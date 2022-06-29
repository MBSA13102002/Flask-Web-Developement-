from flask import Flask, render_template,request,flash,redirect,url_for

app = Flask(__name__)
app.secret_key = "bfewcbweucbwucbn"
@app.route("/",methods=['GET','POST'])
def start():
    if request.method == 'POST':
        num1 = request.form.get("num1")
        num2 = request.form.get("num2")
        # flash("Form Submitted Successfully!!!")  
        return redirect(url_for("sum",int1=num1,int2=num2)) 
    return render_template("index.html")

@app.route("/thankyou")
def bhai():
    return render_template("thankyou.html")

@app.route("/myname/<string:name>")
def myname(name):
    return render_template("myname.html",name = name)

@app.route("/sum/<int:int1>/<int:int2>")
def sum(int1,int2):
    sum_ = int1+int2
    return render_template("num.html",sum_ = sum_)
if __name__ == '__main__':
    app.run(debug=True)


