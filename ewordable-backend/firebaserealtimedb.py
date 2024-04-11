import pyrebase

firebaseConfig = {"apiKey": "AIzaSyCFfW0Mj73KYjRBMyvYTFGtFK2WwwQkj_Y",
  "authDomain": "ewords-4e4f8.firebaseapp.com",
  "projectId": "ewords-4e4f8",
  "storageBucket": "ewords-4e4f8.appspot.com",
  "messagingSenderId": "488707906584",
  "appId": "1:488707906584:web:477d483317683a63e4376d",
  "measurementId": "G-ZZCR4B76GB"

        }

firebase = pyrebase.initialize_app(firebaseConfig)
db = firebase.database()

data = { "name":"john", "age":20 }

db.push(data)
