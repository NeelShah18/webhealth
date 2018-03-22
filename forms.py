from flask_wtf import Form
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired, Email, Length

class SignupForm(Form):
    first_name = StringField('First Name', validators=[DataRequired("Please enter the first name!")])
    last_name = StringField('Last Name', validators=[DataRequired("Please enter the last name!")])
    username = StringField('User Name', validators=[DataRequired("Please enter your username!")])
    email = StringField('Email', validators=[DataRequired("Please enter the email id!"), Email("Please enter valid email address!")])
    password = PasswordField('Password', validators=[DataRequired("Please enter your password!"), Length(min=8, max=16, message="Password should between 8 and 16 charater!")])
    food = StringField('Favourite Food', validators=[DataRequired("Please enter your food details!"), Length(min=3, message="Please enter at least one food item!")])
    exer = StringField('Favourite Excercise', validators=[DataRequired("Please enter your excercise details!"), Length(min=2, message="Please enter at least one excersice!")])
    submit = SubmitField("Sign-Up")

class LoginForm(Form):
    email = StringField("Email", validators=[DataRequired("Please enter your email id!"), Email("Please enter valid email address!")])
    password = PasswordField("Password", validators=[DataRequired("Please enter your password!"), Length(min=8, max=16, message="Password is always between 8 and 16 characters!")])
    submit = SubmitField("Sign-In")

class ForgotForm(Form):
    email = StringField("Email", validators=[DataRequired("Please enter your email id!"), Email("Please enter valid email address!")])
    password = PasswordField("New password", validators=[DataRequired("Please enter your password!"), Length(min=8, max=16, message="Password is always between 8 and 16 characters!")])
    submit = SubmitField("Change")