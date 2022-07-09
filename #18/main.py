
from flask import Flask,render_template,request,g,session,redirect
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
app.secret_key = "dgsgsfgggedg"
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

@app.route("/admin")
def admin():
    if 'user' in session:
        all_entries = db.child("All Submissions").get()
        return render_template("admin.html",all_entries = all_entries)
    return redirect("/login")

@app.route("/login" ,methods=['GET','POST'])
def login():
    if request.method == 'POST':
        session.pop("user",None)
        
        if request.form.get("pass") == 'password' and request.form.get("uname") == "mbsa":
            session['user'] = request.form.get("uname") 
            return redirect("/admin")
    if 'user' in session:
        return redirect("/admin")
    return render_template("login.html")

@app.route('/logout')
def logout():
    session.pop("user",None)
    return redirect("/login")


@app.route("/response/<string:pushkey>/",methods=['GET','POST'])
def response(pushkey):
    data = dict(db.child("All Submissions").child(pushkey).get().val())
    return render_template('response.html',pushkey = pushkey,data = data)




