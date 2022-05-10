from app import app, mongo

from flask import render_template, flash, request, redirect, url_for, session

from flask_mysqldb import MySQL

import re


@app.route("/")
def index():
    return render_template("index.html")

@app.route("/department")
def department():
    return render_template("department.html")

@app.route("/doctors")
def doctors():
    return render_template("doctors.html")

@app.route('/dementia')
def dementia():
    return render_template("dementia.html")

@app.route('/dermatitis')
def dermatitis():
    return render_template("dermatitis.html")

@app.route('/diabetes')
def diabetes():
    return render_template("diabetes.html")

@app.route('/cancer')
def cancer():
    return render_template("cancer.html")

@app.route('/success')
def success():
    return render_template("thank_you.html")

@app.route("/appointment", methods=["GET", "POST"])
def appointment():
    if request.method == 'POST':
        req = request.form

        f_name = req["f_name"]
        l_name = req["l_name"]
        email = req["email"]
        phone = req["phone"]
        appointment_date = req["date"]
        dept = req["department"]
        doctor = req["doctor"]
        has_visited = req["flexRadioDefault"]
        message = req["message"]

        if not len(f_name) >= 2:
            flash("First name must be atleast two characters lenght!", category="warning")
            return render_template("appointment.html")
        elif not len(l_name) >= 2:
            flash("Last name must be atleast two characters lenght!", category="warning")
            return render_template("appointment.html")
        elif not re.match(r"^[A-Za-z0-9\.\+_-]+@[A-Za-z0-9\._-]+[.]\w{3}$", email):
            flash("Invalid email format!", category="warning")
            return render_template("appointment.html")
        # elif not re.match(r"^(^0)(7|8|9){1}(0|1){1}[0–9]{8}$", phone):
        #     flash("Invalid phone number format", category="warning")
        #     return render_template("appointment.html")                 


        #send the data to database
        mongo.db.patient.insert({"f_name":f_name, "l_name":l_name, "email":email, "phone":phone, "appointment_date":appointment_date, "department":dept, "doctor":doctor, "first_time_visit": has_visited, "message_content": message})
        
        # flash("Appointment Submitted Successfully", category="success")
        return redirect(url_for("success"))

    return render_template("appointment.html")
