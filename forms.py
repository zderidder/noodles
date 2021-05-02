from flask_wtf import Form
from wtforms import StringField, IntegerField, TextAreaField, SubmitField
from wtforms import RadioField, validators

class ContactForm():
    name = StringField("Name of the student", [validators.DataRequired(
        "Please enter your name")])

    gender = RadioField('Gender', choices=[('M', 'Male'), ('F', 'Female'),
                                           ('O', 'Others')], default='O')

    address = StringField("Address of the student", [validators.DataRequired(
        "Please enter your address")])

    email = StringField("Email of the student", [validators.DataRequired(
        "Please enter your email"), validators.Email
        ("Please enter your email")])

    submit = SubmitField("Send")

class FunFactForm():
    name = StringField("Enter your name", [validators.DataRequired("Please enter your name")])
    fact = StringField("Enter your fun fact", [validators.DataRequired("What's the point if you don't have a fact?")])

    submit = SubmitField("Send")


