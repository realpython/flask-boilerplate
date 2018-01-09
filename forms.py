from flask_wtf import Form
from wtforms import TextField, PasswordField, StringField
from wtforms.validators import DataRequired, EqualTo, Length,email

# Set your classes here.


class RegisterForm(Form):
    name = StringField(
        'Username', validators=[DataRequired(), Length(min=6)]
    )
    email = StringField(
        'Email', validators=[DataRequired(), Length(min=6, max=254)]
    )
    password = PasswordField(
        'Password', validators=[DataRequired(), Length(min=8, max=100)]
    )
    confirm = PasswordField(
        'Repeat Password',
        [DataRequired(),
        EqualTo('password', message='Passwords must match')]
    )


class LoginForm(Form):
    email = StringField('Email', [DataRequired(),Length(min=6, max=254),email])
    password = PasswordField('Password', [DataRequired()])


class ForgotForm(Form):
    email = StringField(
        'Email', validators=[DataRequired(), Length(min=6, max=254)]
    )
