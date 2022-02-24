from flask import Flask,render_template


app= Flask(__name__)

@app.route('/')
def start():
    var1 = ['python','css','html']
    return render_template("index.html",var_sent = var1)
@app.route('/home')
def home():
    return render_template("home.html")
@app.route('/contact')
def contact():
    return render_template("contact.html")



app.run(debug = True)
