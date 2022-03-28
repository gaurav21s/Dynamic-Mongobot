
## Generated Story 7077939197849866975
* greet
    - utter_greet
* affirmative
    - utter_affirmative

## Generated Story 7077939197849866975
* greet
    - utter_greet
* negative
    - utter_bye
    - action_bye
    - reset_slots

## Generated Story 7077939197849866975
* greet
    - utter_greet
* negative
    - utter_bye
    - action_bye
    - reset_slots

## Generated Story 7077939197849866975
* greet
    - utter_greet
* negative
    - utter_bye
    - action_bye
    - reset_slots

## Generated Story 7077939197849866975
* bye
    - utter_doctor
* negative
    - utter_bye
    - action_bye
    - reset_slots

## Generated Story 7077939197849866975
* bye
    - utter_doctor
* affirmative
    - action_set_provider
    - slot{"providers": "There are 4 providers in your areas. They are 1. Dr Abc, 2. Dr cbd, 3. Dr. xyz, 4, ghf   "}
    - utter_show_provider
    - utter_any_help
* negative
    - utter_bye_treatment
    - action_bye
    - reset_slots

    
## interactive_story_2
* disease{"disease": "constipation"}
    - slot{"disease": "constipation"}
    - action_get_treatment
    - slot{"all_treatments": "1)dietary changes 2)laparoscopic bowel resection 3)nutritional or herbal supplements 4)open bowel resection 5)over the counter laxatives 6)prescription medication 7)regular exercise 8)rehydrate drink more fluids 9)over the counter enema 10)disimpaction of bowel 11)biofeedback "}
    - followup{"name": "utter_treatment"}
    - utter_treatment


## interactive_story_21
* category{"category": "home"}
    - slot{"category": "home"}
    - action_get_treatment_cat
    - slot{"all_treat_cat": "1)dietary changes 2)laparoscopic bowel resection 3)nutritional or herbal supplements 4)open bowel resection 5)over the counter laxatives 6)prescription medication 7)regular exercise 8)rehydrate drink more fluids 9)over the counter enema 10)disimpaction of bowel 11)biofeedback "}
    - followup{"name": "utter_treatment_category"}
    - utter_treatment_category 

## interactive_story_23
* category{"category": "therapies"}
    - slot{"category": "therapies"}
    - action_get_treatment_cat
    - slot{"all_treat_cat": "1)dietary changes 2)laparoscopic bowel resection 3)nutritional or herbal supplements 4)open bowel resection 5)over the counter laxatives 6)prescription medication 7)regular exercise 8)rehydrate drink more fluids 9)over the counter enema 10)disimpaction of bowel 11)biofeedback "}
    - followup{"name": "utter_treatment_category"}
    - utter_treatment_category 


## interactive_story_3
* treatment{"treatment": "enema"}
    - slot{"treatment": "enema"}
    - action_get_treatment_desc
    - slot{"desc_treatment": "<p>Over-the-counter enemas are an effective treatment for constipation for your&nbsp;use at home,&nbsp;Studies have shown that enemas can successfully loosen impacted stools.</p>\n"}
    - followup{"name": "utter_treatment_desc"}
    - utter_treatment_desc

## interactive_story_2
* disease{"disease": "constipation"}
    - slot{"disease": "constipation"}
    - action_get_treatment
    - slot{"all_treatments": "1)dietary changes 2)laparoscopic bowel resection 3)nutritional or herbal supplements 4)open bowel resection 5)over the counter laxatives 6)prescription medication 7)regular exercise 8)rehydrate drink more fluids 9)over the counter enema 10)disimpaction of bowel 11)biofeedback "}
    - followup{"name": "utter_treatment"}
    - utter_treatment

## interactive_story_3
* treatment{"treatment": "enema"}
    - slot{"treatment": "enema"}
    - action_get_treatment_desc
    - slot{"desc_treatment": "<p>Over-the-counter enemas are an effective treatment for constipation for your&nbsp;use at home,&nbsp;Studies have shown that enemas can successfully loosen impacted stools.</p>\n"}
    - followup{"name": "utter_treatment_desc"}
    - utter_treatment_desc


## interactive_story_1
* greet
    - utter_greet
* affirmative
    - utter_affirmative
* disease{"disease": "constipation"}
    - slot{"disease": "constipation"}
    - action_get_treatment
    - slot{"all_treatments": "1)dietary changes 2)laparoscopic bowel resection 3)nutritional or herbal supplements 4)open bowel resection 5)over the counter laxatives 6)prescription medication 7)regular exercise 8)rehydrate drink more fluids 9)over the counter enema 10)disimpaction of bowel 11)biofeedback "}
    - followup{"name": "utter_treatment"}
    - utter_treatment
* treatment{"treatment": "enema"}
    - slot{"treatment": "enema"}
    - action_get_treatment_desc
    - slot{"desc_treatment": "<p>Over-the-counter enemas are an effective treatment for constipation for your&nbsp;use at home,&nbsp;Studies have shown that enemas can successfully loosen impacted stools.</p>\n"}
    - followup{"name": "utter_treatment_desc"}
    - utter_treatment_desc
* bye
    - utter_doctor
* affirmative
    - action_set_provider
    - slot{"providers": "There are 4 providers in your areas. They are 1. Dr Abc, 2. Dr cbd, 3. Dr. xyz, 4, ghf   "}
    - utter_show_provider
    - utter_any_help
* negative
    - utter_bye_treatment
    - action_bye
    - reset_slots


    
## interactive_story_1
* greet
    - utter_greet
* affirmative
    - utter_affirmative
* disease{"disease": "constipation"}
    - slot{"disease": "constipation"}
    - action_get_treatment
    - slot{"all_treatments": "1)dietary changes 2)laparoscopic bowel resection 3)nutritional or herbal supplements 4)open bowel resection 5)over the counter laxatives 6)prescription medication 7)regular exercise 8)rehydrate drink more fluids 9)over the counter enema 10)disimpaction of bowel 11)biofeedback "}
    - followup{"name": "utter_treatment"}
    - utter_treatment
* treatment{"treatment": "enema"}
    - slot{"treatment": "enema"}
    - action_get_treatment_desc
    - slot{"desc_treatment": "<p>Over-the-counter enemas are an effective treatment for constipation for your&nbsp;use at home,&nbsp;Studies have shown that enemas can successfully loosen impacted stools.</p>\n"}
    - followup{"name": "utter_treatment_desc"}
    - utter_treatment_desc
* bye
    - utter_doctor
* negative
    - utter_bye_treatment
    - action_bye
    - reset_slots

    
    
## interactive_story_11
* greet
    - utter_greet
* affirmative
    - utter_affirmative
* disease{"disease": "constipation"}
    - slot{"disease": "constipation"}
    - action_get_treatment
    - slot{"all_treatments": "1)dietary changes 2)laparoscopic bowel resection 3)nutritional or herbal supplements 4)open bowel resection 5)over the counter laxatives 6)prescription medication 7)regular exercise 8)rehydrate drink more fluids 9)over the counter enema 10)disimpaction of bowel 11)biofeedback "}
    - followup{"name": "utter_treatment"}
    - utter_treatment
* category{"category": "therapies"}
    - slot{"category": "therapies"}
    - action_get_treatment_cat
    - slot{"all_treat_cat": "1)dietary changes 2)laparoscopic bowel resection 3)nutritional or herbal supplements 4)open bowel resection 5)over the counter laxatives 6)prescription medication 7)regular exercise 8)rehydrate drink more fluids 9)over the counter enema 10)disimpaction of bowel 11)biofeedback "}
    - followup{"name": "utter_treatment_category"}
    - utter_treatment_category 
* treatment{"treatment": "enema"}
    - slot{"treatment": "enema"}
    - action_get_treatment_desc
    - slot{"desc_treatment": "<p>Over-the-counter enemas are an effective treatment for constipation for your&nbsp;use at home,&nbsp;Studies have shown that enemas can successfully loosen impacted stools.</p>\n"}
    - followup{"name": "utter_treatment_desc"}
    - utter_treatment_desc
* bye
    - utter_doctor
* affirmative
    - action_set_provider
    - slot{"providers": "There are 4 providers in your areas. They are 1. Dr Abc, 2. Dr cbd, 3. Dr. xyz, 4, ghf"}
    - utter_show_provider
    - utter_any_help
* negative
    - utter_bye_treatment
    - action_bye
    - reset_slots



## interactive_story_12
* greet
    - utter_greet
* affirmative
    - utter_affirmative
* disease{"disease": "constipation"}
    - slot{"disease": "constipation"}
    - action_get_treatment
    - slot{"all_treatments": "1)dietary changes 2)laparoscopic bowel resection 3)nutritional or herbal supplements 4)open bowel resection 5)over the counter laxatives 6)prescription medication 7)regular exercise 8)rehydrate drink more fluids 9)over the counter enema 10)disimpaction of bowel 11)biofeedback "}
    - followup{"name": "utter_treatment"}
    - utter_treatment
* category{"category": "therapies"}
    - slot{"category": "therapies"}
    - action_get_treatment_cat
    - slot{"all_treat_cat": "1)dietary changes 2)laparoscopic bowel resection 3)nutritional or herbal supplements 4)open bowel resection 5)over the counter laxatives 6)prescription medication 7)regular exercise 8)rehydrate drink more fluids 9)over the counter enema 10)disimpaction of bowel 11)biofeedback "}
    - followup{"name": "utter_treatment_category"}
    - utter_treatment_category 
* treatment{"treatment": "enema"}
    - slot{"treatment": "enema"}
    - action_get_treatment_desc
    - slot{"desc_treatment": "<p>Over-the-counter enemas are an effective treatment for constipation for your&nbsp;use at home,&nbsp;Studies have shown that enemas can successfully loosen impacted stools.</p>\n"}
    - followup{"name": "utter_treatment_desc"}
    - utter_treatment_desc
* bye
    - utter_doctor
* negative
    - utter_bye_treatment
    - action_bye
    - reset_slots

    
## interactive_story_13
* greet
    - utter_greet
* affirmative
    - utter_affirmative
* disease{"disease": "constipation"}
    - slot{"disease": "constipation"}
    - action_get_treatment
    - slot{"all_treatments": "1)dietary changes 2)laparoscopic bowel resection 3)nutritional or herbal supplements 4)open bowel resection 5)over the counter laxatives 6)prescription medication 7)regular exercise 8)rehydrate drink more fluids 9)over the counter enema 10)disimpaction of bowel 11)biofeedback "}
    - followup{"name": "utter_treatment"}
    - utter_treatment
* category{"category": "therapies"}
    - slot{"category": "therapies"}
    - action_get_treatment_cat
    - slot{"all_treat_cat": "1)dietary changes 2)laparoscopic bowel resection 3)nutritional or herbal supplements 4)open bowel resection 5)over the counter laxatives 6)prescription medication 7)regular exercise 8)rehydrate drink more fluids 9)over the counter enema 10)disimpaction of bowel 11)biofeedback "}
    - followup{"name": "utter_treatment_category"}
    - utter_treatment_category 
* category{"category": "home"}
    - slot{"category": "home"}
    - action_get_treatment_cat
    - slot{"all_treat_cat": "1)dietary changes 2)laparoscopic bowel resection 3)nutritional or herbal supplements 4)open bowel resection 5)over the counter laxatives 6)prescription medication 7)regular exercise 8)rehydrate drink more fluids 9)over the counter enema 10)disimpaction of bowel 11)biofeedback "}
    - followup{"name": "utter_treatment_category"}
    - utter_treatment_category 
* treatment{"treatment": "enema"}
    - slot{"treatment": "enema"}
    - action_get_treatment_desc
    - slot{"desc_treatment": "<p>Over-the-counter enemas are an effective treatment for constipation for your&nbsp;use at home,&nbsp;Studies have shown that enemas can successfully loosen impacted stools.</p>\n"}
    - followup{"name": "utter_treatment_desc"}
    - utter_treatment_desc
* bye
    - utter_doctor
* affirmative
    - action_set_provider
    - slot{"providers": "There are 4 providers in your areas. They are 1. Dr Abc, 2. Dr cbd, 3. Dr. xyz, 4, ghf"}
    - utter_show_provider
    - utter_any_help
* negative
    - utter_bye_treatment
    - action_bye
    - reset_slots

    
## interactive_story_13
* greet
    - utter_greet
* affirmative
    - utter_affirmative
* disease{"disease": "constipation"}
    - slot{"disease": "constipation"}
    - action_get_treatment
    - slot{"all_treatments": "1)dietary changes 2)laparoscopic bowel resection 3)nutritional or herbal supplements 4)open bowel resection 5)over the counter laxatives 6)prescription medication 7)regular exercise 8)rehydrate drink more fluids 9)over the counter enema 10)disimpaction of bowel 11)biofeedback "}
    - followup{"name": "utter_treatment"}
    - utter_treatment
* category{"category": "therapies"}
    - slot{"category": "therapies"}
    - action_get_treatment_cat
    - slot{"all_treat_cat": "1)dietary changes 2)laparoscopic bowel resection 3)nutritional or herbal supplements 4)open bowel resection 5)over the counter laxatives 6)prescription medication 7)regular exercise 8)rehydrate drink more fluids 9)over the counter enema 10)disimpaction of bowel 11)biofeedback "}
    - followup{"name": "utter_treatment_category"}
    - utter_treatment_category 
* category{"category": "home"}
    - slot{"category": "home"}
    - action_get_treatment_cat
    - slot{"all_treat_cat": "1)dietary changes 2)laparoscopic bowel resection 3)nutritional or herbal supplements 4)open bowel resection 5)over the counter laxatives 6)prescription medication 7)regular exercise 8)rehydrate drink more fluids 9)over the counter enema 10)disimpaction of bowel 11)biofeedback "}
    - followup{"name": "utter_treatment_category"}
    - utter_treatment_category 
* treatment{"treatment": "enema"}
    - slot{"treatment": "enema"}
    - action_get_treatment_desc
    - slot{"desc_treatment": "<p>Over-the-counter enemas are an effective treatment for constipation for your&nbsp;use at home,&nbsp;Studies have shown that enemas can successfully loosen impacted stools.</p>\n"}
    - followup{"name": "utter_treatment_desc"}
    - utter_treatment_desc
* bye
    - utter_doctor
* negative
    - utter_bye_treatment
    - action_bye
    - reset_slots
