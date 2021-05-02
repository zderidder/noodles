from flask_wtf import Form
from wtforms import StringField, IntegerField, TextAreaField, SubmitField
from wtforms import RadioField, SelectField, validators


class ContactForm(Form):
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


class FunFactForm(Form):
    name = StringField("name", [validators.DataRequired()])
    fact = StringField("fun fact", [validators.DataRequired()])

    submit = SubmitField("Send")


