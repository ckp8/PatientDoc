from flask import render_template, request, redirect, url_for
from applications import app, db
from flask import Flask
from applications.forms import BasicForm, CreateAppt
from applications.models import Patients, Doctor,Appointment

@app.route('/')
@app.route('/home')
def home():
    return render_template("home.html")

@app.route('/create', methods = ['GET','POST'])
def create():
    message = ""
    form = BasicForm()
    if request.method == 'POST':
        info = Patients(first_name = form.first_name.data,
        last_name = form.last_name.data,
        dob = form.dob.data)
       
        
        # dob = form.dob.data
        
        db.session.add(info)
        db.session.commit()
        
        
       
    return render_template('create.html', form = form, message = message)

@app.route ('/view')
def view():
    all_patients = Patients.query.all()
    patient_string = ""
    for patient in all_patients:
        patient_string += "<br>"+ patient.first_name + patient.last_name + patient.dob
    return patient_string
    # return render_template('view.html')

# @app.route('/view/<name>', methods = ['GET'])
# def appt():

@app.route('/add')
def add():
    form = CreateAppt()
    return render_template("add.html", form = form)