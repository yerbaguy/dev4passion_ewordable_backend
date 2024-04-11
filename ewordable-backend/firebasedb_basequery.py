import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore
#from google.cloud.firestore_v1.base_query import FieldFilter,iOr

cred = credentials.Certificate('ewords-4e4f8-firebase-adminsdk-u8kct-3bc2f120d8.json')
firebase_admin.initialize_app(cred)

db = firestore.client()

#object1 = {
#        "name":"bart",
#        "age":43
#        }

#object2 = {
#        "name":"bartek",
#        "age":43
#        }

#data = [object1, object2]

#for record in data:
#    doc_ref = db.collection(u'Users').document(record['name'])
#    doc_ref.set(record)

docs = (
        db.collection("Words")
        .stream()
        )

documents_list = []

for doc in docs:
    doc_data = doc.to_dict()
    documents_list.append(doc_data)


for doc_data in documents_list:
    print("doc_data", doc_data)


print("doc_data_len", len(documents_list))

for doc_data1 in documents_list:
    print("doc_data1", doc_data1)

for doc_data2 in documents_list:
    print("doc_data2", doc_data2["definition"]["definitions"][0]["definition"])


#for i in range(len(documents_list)):
#print("doc_data11", documents_list[0]["definition"])

print("doc_data_word", documents_list[0]["word"])
print("doc_data_definition", documents_list[0]["definition"])

documents_list[0]["definition"]["definitions"]
print("doc_data_definitions", documents_list[0]["definition"]["definitions"][0]["definition"])

documents_list_definition_example = documents_list[0]["definition"]["definitions"][0]["definition"]
print("documents_list_definition_example", documents_list_definition_example)


documents_list_definition_example1 = documents_list[0]["definition"]["definitions"][0]["example"]
print("documents_list_definition_example1", documents_list_definition_example1)

documents_list_definition_example[0][0]
#print("documents_list_definition_example", documents_list_definition_example[0][0])


documents_list[0]["phonetics"]
print("documents_list_phontics", documents_list[0]["phonetics"][0]["text"])


#definitions = documents_list[0]["definition"]
#print("doc_data_definitions", definitions[0])


dataStream_meanings_partOfSpeech = documents_list[0]["definition"]
print("doc_data_meanings_partOfSpeech", dataStream_meanings_partOfSpeech["partOfSpeech"])
dataStream_meanings_partOfSpeech["partOfSpeech"][0][0]


