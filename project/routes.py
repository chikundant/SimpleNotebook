from project import app
from project.forms import LoginForm, RegisterForm, NoteForm
from flask import render_template, url_for, redirect
from flask_login import login_required, logout_user, current_user, login_user
from project import db
from project.db import MySQLNotes
from project.models import User


@app.route("/")
@app.route("/index")
@login_required
def index():
    return render_template('index.html')


@app.route("/login", methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('index'))

    form = LoginForm()

    if form.validate_on_submit():
        user = User()
        user.load(db.get_by_field('*', 'user', 'username', form.username.data)[0])

        if user is None or not user.check_password(form.password.data):
            return redirect(url_for('login'))

        login_user(user, remember=form.remember_me.data)

        return redirect(url_for('index'))
    return render_template('login.html', form=form)


@app.route("/logout")
def logout():
    logout_user()
    return redirect(url_for('index'))


@app.route("/register", methods=['GET', 'POST'])
def register():
    if current_user.is_authenticated:
        return redirect(url_for('index'))

    form = RegisterForm()

    if form.validate_on_submit():
        user = User()
        user.set_password(form.password.data)
        db.insert_field('user', form.username.data, form.email.data, user.password_hash)
        return redirect(url_for('login'))
    return render_template('register.html', form=form)


@app.route("/add_note", methods=['GET', 'POST'])
@login_required
def add_note():
    form = NoteForm()
    db_note = MySQLNotes()
    if form.validate_on_submit():
        db_note.insert_field('note', current_user.get_id(), form.title.data, form.body.data)
        return redirect(url_for('index'))
    return render_template("add.html", form=form)


@app.route("/my_note", methods=['GET', 'POST'])
def my_note():
    return 'my_note'
