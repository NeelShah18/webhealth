from flask_wtf import Form
from wtforms import StringField, PasswordField, SubmitField, SelectMultipleField
from wtforms.validators import DataRequired, Email, Length
from wtforms import SelectField

class SignupForm(Form):
    colours = [(0,'Red'), (1,'Blue')]
    first_name = StringField('First name', validators=[DataRequired("Please enter the first name")])
    last_name = StringField('Last name', validators=[DataRequired("Please enter the last name")])
    username = StringField('User name', validators=[DataRequired("Please enter your username")])
    email = StringField('Email', validators=[DataRequired("Please enter the email id"), Email("Please enter valid email address.")])
    password = PasswordField('Password', validators=[DataRequired("Please enter your password"), Length(min=8, max=16, message="Password should between 8 and 16 charater")])
    state = SelectField('Chouse your state', choices=colours)
    submit = SubmitField("Singn up")

class LoginForm(Form):
    email = StringField("Email", validators=[DataRequired("Please enter your email id"), Email("Please enter valid email address")])
    password = PasswordField("password", validators=[DataRequired("Please enter your password"), Length(min=8, max=16, message="Password is always between 8 and 16 characters")])
    submit = SubmitField("Sign in")