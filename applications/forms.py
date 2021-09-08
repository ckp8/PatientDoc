from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, SelectField, IntegerField,DateField
from wtforms.validators import DataRequired


class BasicForm(FlaskForm):
    first_name = StringField('First Name')
    last_name = StringField('Last Name')
    dob = StringField("choose date")

    submit = SubmitField('register')

class CreateAppt(FlaskForm):
      uniqueID = StringField("enter id")
      date = StringField("choose date")

      submit = SubmitField('add Appointment')


   