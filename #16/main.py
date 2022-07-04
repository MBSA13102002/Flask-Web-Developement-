
from flask import Flask,render_template,request
# ========================================================
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

db = firebase.database()
# ===========================================================
app = Flask(__name__)

@app.route("/",methods=['GET','POST'])
def start():
    if request.method == 'POST':

        name = request.form.get("name")
        email = request.form.get("email")
        subject = request.form.get("subject")
        message = request.form.get("message")

        data = {
            "name":name,
            "email":email,
            "subject":subject,
            "message":message

        }
        db.child("All Submissions").push(data)
        return render_template('index.html')
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)