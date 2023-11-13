from flask import Flask, render_template, request

app=Flask(__name__)

@app.route("/")
def home():
    return render_template('home.html')

@app.route("/design")
def design():
    return render_template('design.html')

@app.route("/form")
def form():
    return render_template('formMainBasic.html')

@app.route("/upload" , methods=["GET","POST"])
def upload():
    if request.method=="POST":
        name = request.form.get("Name")
        phone = request.form.get("Phone")
        email = request.form.get("email")
        linkedIn = request.form.get("LinkedIn")
        about= request.form.get("about")

        print(name,phone,email,linkedIn,about)
        return"Uploaded"

app.run(debug=True)