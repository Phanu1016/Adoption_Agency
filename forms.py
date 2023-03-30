from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, SelectField, BooleanField
from wtforms.validators import InputRequired, Optional, URL, NumberRange, AnyOf

class AddPetForm(FlaskForm):
    """ Pet form for when adding new pet to adoption center """
    name = StringField("Pet Name: ",  validators=[InputRequired(message="Name cannot be empty.")])
    species = SelectField("Species: ",  choices=[('cat', 'Cat'), ('dog', 'Dog'), ('porcupine', "Porcupine")], coerce=str, validators=[InputRequired(message="Species cannot be empty."), AnyOf(values=['cat', 'dog', 'porcupine'], message="Species can only be cat, dog, or porpupine")])
    photo_url = StringField("Photo (URL): ",  validators=[URL(message="Not an URL"), Optional()])
    age = IntegerField("Age: ",  validators=[NumberRange(min=0, max=30, message="Age cannot be negative or above 30."), Optional()])
    notes = StringField("Note: ",  validators=[Optional()])

class EditPetForm(FlaskForm):
    """ Pet form for when editting existing pet in adoption center """
    photo_url = StringField("Photo (URL): ",  validators=[URL(message="Not an URL"), Optional()])
    notes = StringField("Note: ",  validators=[Optional()])
    available = BooleanField("Available")
