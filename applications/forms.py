# from flask_wtf import FlaskForm
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, SelectField, IntegerField,DateField
from wtforms.validators import DataRequired


class BasicForm(FlaskForm):
    first_name = StringField('First Name',validators=[DataRequired(message = "enter a name")])
    last_name = StringField('Last Name',validators=[DataRequired(message = "enter a name")])
    dob = StringField("choose date",validators=[DataRequired(message = "enter a name")])
    submit = SubmitField('register')

class CreateAppt(FlaskForm):
      uniqueID = StringField("enter id",validators=[DataRequired(message = "enter your uniqueID")])
      date = StringField("choose date")

      submit = SubmitField('add Appointment')
    
class CancelAppt(FlaskForm):
      uniqueID = StringField("enter id",validators=[DataRequired(message = "enter a uniqueID")])
      date = StringField("choose date",validators=[DataRequired(message = "enter a the date")])

      submit = SubmitField('cancel Appointment')



   