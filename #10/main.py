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

if __name__ == '__main__':
    app.run(debug=True)


