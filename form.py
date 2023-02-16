from wtforms import Form
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, Field, FormField, SelectField, RadioField
from wtforms.fields import EmailField

class UserForm(Form):
    id = StringField('id')
    name = StringField('name')
    lastname = StringField('lastname')
    email = EmailField('email')


