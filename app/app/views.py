from app import app


from flask import render_template, request



@app.route("/")#url
def index():
    name = request.args.get("name")
    return render_template("public/index.html", name = "ge")

@app.route("/about")
def about():
    return "<h1 style='color: red'>About!!!!!</h1>"





@app.route("/public/index.html")
def point():
     
    return render_template("public/index.html")