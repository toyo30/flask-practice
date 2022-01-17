import os
import smtplib
from app import app


from flask import render_template, request

students = []

@app.route("/lecture")#url
def foo():
    # name = request.args.get("name")
    return render_template("lecture.html")



@app.route("/registrants")
def registrants():
    return render_template("registered.html", students = students)



@app.route("/register", methods=["POST"])
def register():
    studnents = []
    name = request.form.get("name")
    # email = request.form.get("email")
    dorm = request.form.get("dorm")
    if not name or not dorm:
        return render_template("failure.html")
    # message = "You are registered!"
    # server = smtplib.SMTP("smpt.gmail.com", 587)
    # server.starttls()
    # server.login("jharverd@cs50.net", os.getenv("PASSWORD"))
    # server.sendmail("jhavard@cs50.net", email, message)
    return render_template("success.html")
    #     return "failure"
    # students.append(f'{name} for {dorm}')

    # if students.length == 0:
    #     return render_template("success.html")
    # return redirect("/registrants")
    
    #Todo

