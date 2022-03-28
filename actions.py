# -*- coding: utf-8 -*-
import datetime
import pandas as pd
from typing import Dict, Text, Any, List, Union
from rasa_sdk.events import SlotSet, AllSlotsReset, Restarted, ConversationPaused
from rasa_sdk import Action
from rasa_sdk import ActionExecutionRejection
from rasa_sdk import Tracker
from rasa_sdk.executor import CollectingDispatcher
from rasa_sdk.forms import FormAction, REQUESTED_SLOT
from rasa_sdk.events import SlotSet, UserUtteranceReverted, ConversationPaused, FollowupAction, Form
import json

from pymongo import MongoClient

client = MongoClient('mongodb://localhost:27017')
db = client['rodin']
table = db.topics


class GetTreatments(Action):
    def name(self):
        return 'action_get_treatment'

    def run(self, dispatcher, tracker, domain):
        dis = tracker.get_slot('disease')
        disease = '-'.join(dis.split(' '))
        reg_d = 'for-condition-' + disease
        treats = table.find({"id": {"$regex": reg_d}, "type": "types/treatments"}, {"_id": 1})
        j = 1
        treatments = ''
        for result in treats:
            treat = result["_id"].split('/')[1].split('-for-')[0]
            treatments += str(j) + ')' + ' '.join(treat.split('-')) + ' '
            j += 1

        cond_disease = 'conditions/' + disease
        query2 = {"id": cond_disease}
        test4 = table.find(query2, {"relations.relations/modules/belongs-to-module": 1})
        for t in test4:
            module = t['relations']['relations/modules/belongs-to-module']
        mod = list(module.keys())
        root_module = mod[0].split('/')[-1]
        link = "https://www2.mywiserhealth.com/" + root_module + '/' + disease + '/list/route/1'
        # print(treatments)
        # d2 = '-'.join(disease.split(' '))
        # id_query='treatments/dietary-changes-for-condition-'+d2
        # result = table.find_one({"id":id_query})
        # treatment = result["attributes"]["ebm-summary"]
        return [SlotSet("all_treatments", treatments), SlotSet("link", link), FollowupAction('utter_treatment')]


class GetTreatmentDesc(Action):
    def name(self):
        return 'action_get_treatment_desc'

    def run(self, dispatcher, tracker, domain):
        dis = tracker.get_slot('disease')
        disease = '-'.join(dis.split(' '))
        reg_d = 'for-condition-' + disease
        treatment = tracker.get_slot('treatment')
        choice = '-'.join(treatment.split(' '))
        query = {'$and': [{"id": {"$regex": reg_d}}, {"id": {"$regex": choice}}, {"type": "types/treatments"}]}
        # test3=table.find({"id": {"$regex":reg_d},"id":{"$regex":choice},"type":"types/treatments"},{"attributes.ebm-summary":1})
        test3 = table.find(query, {"attributes.ebm-summary": 1})

        for t in test3:
            result = t['attributes']['ebm-summary']
        # d2 = '-'.join(disease.split(' '))
        # id_query='treatments/dietary-changes-for-condition-'+d2
        # result = table.find_one({"id":id_query})
        treatment_desc = result  # result["attributes"]["ebm-summary"]
        return [SlotSet("desc_treatment", treatment_desc), FollowupAction('utter_treatment_desc')]


class SetProvider(Action):
    def name(self):
        return 'action_set_provider'

    def run(self, dispatcher, tracker, domain):
        providers = "There are 4 providers in your areas. They are 1. Dr Abc, 2. Dr cbd, 3. Dr. xyz, 4. Dr. ghf"
        return [SlotSet("providers", providers), FollowupAction('utter_show_provider')]


class GetTreatmentCat(Action):
    def name(self):
        return 'action_get_treatment_cat'

    def run(self, dispatcher, tracker, domain):
        cat_dict = {'prescription medications': "Prescription Medications",
                    'home': "At Home / Lifestyle",
                    'medical procedures': "Medical Procedures / Services",
                    'equipments': "Equipment / Devices",
                    'therapies': "Therapies",
                    'over the counter': "Over-the-Counter Medications / Supplements"
                    }
        dis = tracker.get_slot('disease')
        disease = '-'.join(dis.split(' '))
        reg_d = 'for-condition-' + disease
        category = tracker.get_slot('category')
        choice = cat_dict[category]
        query = {'$and': [{"id": {"$regex": reg_d}}, {"attributes.treatment-category": {"$regex": choice}},
                          {"type": "types/treatments"}]}
        # test3=table.find({"id": {"$regex":reg_d},"id":{"$regex":choice},"type":"types/treatments"},{"attributes.ebm-summary":1})
        test3 = table.find(query, {"id": 1})
        tree = ''
        j = 1
        for r in test3:
            treat = r["_id"].split('/')[1].split('-for-')[0]
            tree += str(j) + ')' + ' '.join(treat.split('-')) + ' '
            j += 1
        # d2 = '-'.join(disease.split(' '))
        # id_query='treatments/dietary-changes-for-condition-'+d2
        # result = table.find_one({"id":id_query})
        cat_treat = tree  # result["attributes"]["ebm-summary"]
        return [SlotSet("all_treat_cat", cat_treat), FollowupAction('utter_treatment_category')]


class ActionGoodBye(Action):
    def name(self):
        return 'action_bye'

    def run(self, dispatcher, tracker, domain):
        # dispatcher.utter_template("utter_bye",tracker)
        return [AllSlotsReset()]


class ActionRestart(Action):
    def name(self):
        return 'action_restart'

    def run(self, dispatcher, tracker, domain):
        # dispatcher.utter_template("utter_bye",tracker)
        return [Restarted()]


class ActionListen(Action):
    """The first action in any turn - bot waits for a user message.
	The bot should stop taking further actions and wait for the user to say
	something."""

    def name(self) -> Text:
        return 'action_listen'

    def run(self, dispatcher, tracker, domain):
        return []
