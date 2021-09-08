from flask import render_template, request, redirect, url_for
from applications import app, db
from flask import Flask
from applications.forms import BasicForm

@app.route('/')
@app.route('/home')
def home():
    return render_template("home.html")

@app.route('/create', methods = ['GET','POST'])
def create():
    message = ""
    form = BasicForm()
    if request.method == 'POST':
        first_name = form.first_name.data
        last_name = form.last_name.data
        dob = form.dob.data
        
        db.session.add(form)
        db.session.commit()
        
        if len(first_name) == 0 or len(last_name) == 0:
            message = "Please enter name"
        else:
            message = f'Thank you, {first_name} {last_name} for booking an appointment on the {dob}'
    return render_template('create.html', form = form, message = message)

@app.route ('/view')
def view():
    return render_template('view.html')