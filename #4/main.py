from flask import Flask,render_template


app= Flask(__name__)

@app.route('/')
def start():
    var1 = ['python','css','html']
    return render_template("index.html",var_sent = var1)


app.run(debug = True)
