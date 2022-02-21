from flask import Flask,render_template
app = Flask(__name__)
#app = Flask(__name__,static_folder="gh",template_folder="mm") (attributes to change the template folder & static folder name)

@app.route("/")
def start():
    return render_template('index.html') #render_template is used to render HTML template on the server
  


app.run(debug = True)
