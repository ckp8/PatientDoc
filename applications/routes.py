from flask import render_template, request, redirect, url_for
from applications import app, db
from flask import Flask
from applications.forms import BasicForm, CreateAppt, CancelAppt
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
        patient_string += "<br>"+ patient.first_name + patient.last_name + patient.dob + str(patient.id)
    return patient_string
    # return render_template('view.html')

# @app.route('/view/<name>', methods = ['GET'])
# def appt():

@app.route('/add', methods = ['GET','POST'])
def add():
    form = CreateAppt()
    if request.method == 'POST':

        appt = Appointment(patient_id = form.uniqueID.data,
        
        date = form.date.data)

        
        
       
        exists = db.session.query(Patients.id).filter_by(id=form.uniqueID.data).first() is not None

        if exists:

           


        
       
        
        # dob = form.dob.data
        
          db.session.add(appt)
          db.session.commit()
        else:

           return "you need to register"
    return render_template('add.html',form=form)

@app.route ('/cancel',methods = ['GET','POST'])
def cancel():
    form = CancelAppt()
    if request.method == 'POST':
        exists = db.session.query(Appointment.patient_id).filter_by(patient_id=form.uniqueID.data, date=form.date.data).first() is not None
        msg = ""
        if exists:
            Appointment.query.filter_by(patient_id=form.uniqueID.data, date=form.date.data).delete()
            db.session.commit()
            msg ="deleted successfully"

        return render_template('cancel.html',form=form, message=msg)
    return render_template('cancel.html',form=form)


# @app.route('/update', methods = ['GET','POST'])
# @app.route('/update', methods = ['GET','POST'])
# def update():
#     msg = ''
#     form = CreateAppt()
#     if request.method == 'POST':
#         exists = db.session.query(Appointment.patient_id).filter_by(patient_id=form.uniqueID.data).first() is not None
#         print (exists)
#         if exists:
#             print ("exists")    
#             db.session.query(Appointment.patient_id).filter(Appointment.patient_id == form.uniqueID.data).update({'date': form.date.data})
#             db.session.commit()
#             msg ="updated successfully"
#     return render_template('update.html',form=form, message=msg)

@app.route('/update', methods = ['GET','POST'])
def update():
    msg = ''
    form = CreateAppt()
    if request.method == 'POST':
        exists = db.session.query(Appointment.patient_id).filter_by(patient_id=form.uniqueID.data).first() is not None
        print (exists)
        if exists:
            print ("exists")    
            db.session.query(Appointment.patient_id).filter(Appointment.patient_id == form.uniqueID.data).update({'date': form.date.data})
            db.session.commit()
            msg ="updated successfully"
    return render_template('update.html',form=form, message=msg)


@app.route ('/views')
def views():
    all_appt = Appointment.query.all()
    appt_string = ""
    for appt in all_appt:
        appt_string += "<br>"+ str(appt.patient_id) + appt.date
    return appt_string