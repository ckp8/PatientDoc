from applications import db

class Patients (db.Model):
    id = db.Column(db.Integer, primary_key = True)
    first_name = db.Column(db.String(30),nullable= False)
    last_name = db.Column(db.String(30), nullable = False)

class Doctor (db.Model):
    id = db.Column(db.Integer, primary_key = True)
    first_name = db.Column(db.String(30),nullable= False)
    last_name = db.Column(db.String(30), nullable = False)
    patient_id = db.Column(db.Integer, db.ForeignKey('patient.id'), nullable=False)
    
class Appointment (db.Model):
    id = db.Column(db.Integer,primary_key = True)
    patient_id = db.Column(db.Integer, db.ForeignKey('patient.id'), nullable=False)
    doctor_id = db.Column(db.Integer, db.ForeignKey('doctor.id'), nullable=False)

