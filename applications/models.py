from applications import db
from datetime import datetime


class Patients (db.Model):
    id = db.Column(db.Integer, primary_key = True)
    first_name = db.Column(db.String(30),nullable= False)
    last_name = db.Column(db.String(30), nullable = False)
    doctors = db.relationship('Doctor', backref = 'patientdoc')
    appt = db.relationship('Appointment', backref = 'patientappt')
    
    dob = db.Column(db.String(30), nullable = False)

class Doctor (db.Model):
    id = db.Column(db.Integer, primary_key = True)
    first_name = db.Column(db.String(30),nullable= False)
    last_name = db.Column(db.String(30), nullable = False)
    patient_id = db.Column(db.Integer, db.ForeignKey('patients.id'), nullable=False)
    
class Appointment (db.Model):
    id = db.Column(db.Integer,primary_key = True)
    patient_id = db.Column(db.Integer, db.ForeignKey('patients.id'), nullable=False)
    date = db.Column(db.DateTime,nullable= False)

