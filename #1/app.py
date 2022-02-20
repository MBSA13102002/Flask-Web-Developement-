#importing Flask Class from flask Module
from flask import Flask
#Initializing Flask Class wiht __name__ parameter.
app = Flask(__name__)

#function for '/' route
@app.route("/")
def start():
    return "Hello World kkk"
  
#function for '/mbsa' route
@app.route("/mbsa")
def mbsa():
    return "Hello World MBSA"


app.run #for production level.
# app.run(debug = True) { for realtime hot reloading}

