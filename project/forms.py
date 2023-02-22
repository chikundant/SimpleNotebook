from flask_wtf import FlaskForm
from wtforms import SubmitField, StringField, PasswordField, EmailField, BooleanField, TextAreaField, DateField
from wtforms.validators import EqualTo, ValidationError, DataRequired
from project.db import MySQLUser
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
    password2 = PasswordField('Repeat password', validators=[EqualTo('password')])
    submit = SubmitField("Register")

    def validate_username(self, username):
        db = MySQLUser()
        data = db.get_by_field('*', 'username', username.data)
        user = User()
        if data is not None:
            user.load(data[0])
        if user.username is not None:
            raise ValidationError('Please use a different username.')

    def validate_email(self, email):
        db = MySQLUser()
        data = db.get_by_field('*', 'email', email.data)
        user = User()
        if data is not None:
            user.load(data[0])
        if user.email is not None:
            raise ValidationError('Please use a different email address.')


class NoteForm(FlaskForm):
    title = StringField('Title')
    body = TextAreaField('Text')
    save = SubmitField('Save')
    delete = SubmitField('Delete')
    search = StringField('Search')
    submit = SubmitField('Find')
    time = DateField('Time', format='%m-%d-%y')

