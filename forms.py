from flask_wtf import Form
from wtforms import StringField, TextAreaField, SubmitField
from wtforms import RadioField, SelectField, validators

class ContactUs(Form):
    name = StringField("name")

    email = StringField("email")

    problem = SelectField("problem")

    description = TextAreaField("description")

    submit = SubmitField("Send")


class FunFactForm(Form):
    name = StringField("name")
    fact = StringField("fun fact")

    submit = SubmitField("Send")

class RestaurantForm(Form):
    email = StringField("email")
    restaurant = StringField("restaurant")
    address = StringField("address")
    submit = SubmitField("Send")


class HomemadeForm(Form):
    email = StringField("email")
    recipe = StringField("recipe")
    link = StringField("link")

    submit = SubmitField("Send")

