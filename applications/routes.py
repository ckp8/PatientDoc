from flask import render_template, request, redirect, url_for
from applications import app, db
from flask import Flask
from applications.forms import BasicForm
from applications.models import Patients

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
        last_name = form.last_name.data)
       
        
        # dob = form.dob.data
        
        db.session.add(info)
        db.session.commit()
        
        
       
    return render_template('create.html', form = form, message = message)

@app.route ('/view')
def view():
    return render_template('view.html')