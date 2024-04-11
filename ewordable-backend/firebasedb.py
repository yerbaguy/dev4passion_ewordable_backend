import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore

cred = credentials.Certificate('ewords-4e4f8-firebase-adminsdk-u8kct-3bc2f120d8.json')
firebase_admin.initialize_app(cred)

db = firestore.client()

object1 = {
        "name":"bart",
        "age":43
        }

object2 = {
        "name":"bartek",
        "age":43
        }

data = [object1, object2]

for record in data:
    doc_ref = db.collection(u'Users').document(record['name'])
    doc_ref.set(record)
