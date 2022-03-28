from pymongo import MongoClient
client = MongoClient('mongodb://localhost:27017')
db = client['rodin']
table = db.topics
results = table.find({"name": "Dietary changes"})
'''
for result in results:
	print(result["attributes"]["ebm-summary"],result["id"])

test = table.find_one({"id":"treatments/dietary-changes-for-condition-astigmatism"})
print (test["attributes"]["ebm-summary"])
'''
disease='constipation'
reg_d = 'for-condition-'+disease
test2=table.find({"id": {"$regex":reg_d},"type":"types/treatments"},{"_id":1})
j=1
treatments=''
for r in test2:
	treat=r["_id"].split('/')[1].split('-for-')[0]
	treatments+=str(j)+')'+' '.join(treat.split('-'))+' '
	j+=1
#print(treatments)
choice='enema'
test3=table.find({"id": {"$regex":reg_d},"id":{"$regex":choice},"type":"types/treatments"},{"attributes.ebm-summary":1})
#print(test3)
#print(test3['attributes']['ebm-summary'])
#for t in test3:
#	print (t['attributes']['ebm-summary'])
#query ="db.topics.find({"id": {$regex:/gout/},"type":"types/treatments"},{"_id":1}).pretty()"
#db.types.find({},{"name":1}).pretty()
#db.topics.find({"id": {$regex:/constipation/},"type":"types/treatments"},{"_id":1,"attributes.treatment-category":1}).pretty()
#db.topics.find({$and:[{"id": {"$regex":'for-condition-constipation'}},{"id":{"$regex":'herbal-supplements'}},{"type":"types/treatments"}]},{"attributes.ebm-summary":1}).pretty()
cat_dict={'prescription medications':"Prescription Medications",
				  'home':"At Home / Lifestyle",
				  'medical procedures':"Medical Procedures / Services",
				  'equipments':"Equipment / Devices",
				  'therapies':"Therapies",
				  'over the counter':"Over-the-Counter Medications / Supplements"
				  }
disease = 'constipation'
reg_d = 'for-condition-'+disease
category = 'home'
choice = cat_dict[category]
query ={'$and':[{"id": {"$regex":reg_d}},{"attributes.treatment-category":{"$regex":choice}},{"type":"types/treatments"}]}
#test3=table.find({"id": {"$regex":reg_d},"id":{"$regex":choice},"type":"types/treatments"},{"attributes.ebm-summary":1})
test3 = table.find(query,{"_id":1})
tree=''
for r in test3:
	treat=r["_id"].split('/')[1].split('-for-')[0]
	tree+=str(j)+')'+' '.join(treat.split('-'))+' '
	j+=1
print(tree)
cond_disease = 'conditions/'+disease
query2={"id" : cond_disease}
test4 = table.find(query2,{"relations.relations/modules/belongs-to-module":1})
for t in test4:
       module= t['relations']['relations/modules/belongs-to-module']
mod=list(module.keys())
root_module=mod[0].split('/')[-1]
link = "https://www2.mywiserhealth.com/"+root_module+'/'+disease+'/list/route/1'
print(link)
'''
"treatment-category" : {
                                "required" : false,
                                "type" : "string",
                                "id" : "treatment-category",
                                "enum" : [
                                        "Medical Procedures / Services",
                                        "Equipment / Devices",
                                        "Prescription Medications",
                                        "Therapies",
                                        "At Home / Lifestyle",
                                        "Over-the-Counter Medications / Supplements",
                                        "Preventive Care / Consultations",
                                        "Other"
                                ]
                        }
'''