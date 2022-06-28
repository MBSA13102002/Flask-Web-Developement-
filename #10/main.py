from flask import Flask, render_template,request,flash

app = Flask(__name__)
app.secret_key = "bfewcbweucbwucbn"
@app.route("/",methods=['GET','POST'])
def start():
    if request.method == 'POST':
        mobno = request.form.get("mobno")  
        flash("Form Submitted Successfully!!!")  
        return render_template("index.html")  
    return render_template("index.html")

@app.route("/myname/<string:name>")
def myname(name):
    return render_template("myname.html",name = name)

@app.route("/sum/<int:int1>/<int:int2>")
def sum(int1,int2):
    sum_ = int1+int2
    return render_template("num.html",sum_ = sum_)
if __name__ == '__main__':
    app.run(debug=True)


