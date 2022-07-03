#IMporting & Configuring Database
from firebase import Firebase
config = {
  "apiKey": "AIzaSyAyD9nGwpDt3tfejBKPK6EcQHHjKPP8g14",
  "authDomain": "first-flask-app-7240a.firebaseapp.com",
  "projectId": "first-flask-app-7240a",
  "storageBucket": "first-flask-app-7240a.appspot.com",
  "messagingSenderId": "1003956175326",
  "appId": "1:1003956175326:web:156ceace7ecb34a951dd4f",
  "measurementId": "G-GYS34K731Q",
  "databaseURL":"https://first-flask-app-7240a-default-rtdb.firebaseio.com/"
}
firebase = Firebase(config)

db = firebase.database() #Initializing Database in Firebase



# data = {
#   'name':'sai',
#   'age':20,
#   'phone':7515616
# }



# db.set(data)
# db.push(data)
# db.update({
#   'address':'india'
# })



# for i in range(7):
#   db.push({
#     'name':'sai_'+str(i+1),
#     'age':20+i
# })



# data = db.get()
# for item in data.each():
#   print(item.key())



