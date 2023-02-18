from flask_wtf import FlaskForm
from wtforms import SubmitField, StringField, PasswordField, EmailField, BooleanField
from wtforms.validators import EqualTo, ValidationError, DataRequired
from project import db
from project.models import User


class LoginForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    remember_me = BooleanField('Remember Me')
    submit = SubmitField('Sign In')


class RegisterForm(FlaskForm):
    username = StringField('Username')
    email = EmailField('Email')
    password = PasswordField('Password')
    password2 = PasswordField('Password', validators=[EqualTo('password')])
    submit = SubmitField("Register")

    def validate_username(self, username):
        data = db.get_by_field('*', 'user', 'username', username.data)
        user = User()
        if data is not None:
            user.load(data[0])
        if user.username is not None:
            raise ValidationError('Please use a different username.')

    def validate_email(self, email):
        data = db.get_by_field('*', 'user', 'email', email.data)
        user = User()
        if data is not None:
            user.load(data[0])
        if user.email is not None:
            raise ValidationError('Please use a different email address.')