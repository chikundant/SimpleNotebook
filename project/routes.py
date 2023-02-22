from project import app
from project.forms import LoginForm, RegisterForm, NoteForm
from flask import render_template, url_for, redirect, request
from flask_login import login_required, logout_user, current_user, login_user
from project.db import MySQLNotes, MySQLUser
from project.models import User


@app.route("/", methods=['POST', 'GET'])
@app.route("/index", methods=['POST', 'GET'])
@login_required
def index():
    db = MySQLNotes()
    form = NoteForm()
    notes = db.get_by_field('*', 'user_id', current_user.get_id())
    if notes:
        return render_template('index.html', notes=notes, form=form)
    else:
        return render_template('not_found.html', form=form)


@app.route("/search", methods=['POST', 'GET'])
@login_required
def search():
    db = MySQLNotes()
    form = NoteForm()
    if request.method == 'POST':
        if form.is_submitted():
            print(form.time._value())
            print(form.search.data)

            if not form.time._value() and form.search.data != '':
                notes = db.find_field_by_one_definition('title', current_user.get_id(), form.search.data)
                if notes:
                    return render_template('index.html', notes=notes, form=form)
            elif form.time._value() and form.search.data == '':
                notes = db.find_field_by_one_definition('time', current_user.get_id(), form.time._value())
                if notes:
                    return render_template('index.html', notes=notes, form=form)

            elif form.time._value() and form.search.data != '':
                notes = db.find_field_by_two_definitions(current_user.get_id(), form.time._value(), form.search.data)
                if notes:
                    return render_template('index.html', notes=notes, form=form)

    return render_template('not_found.html', form=form)


@app.route("/login", methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('index'))

    form = LoginForm()
    db = MySQLUser()

    if form.validate_on_submit():
        user = User()
        data = db.get_by_field('*', 'username', form.username.data)
        if data:
            user.load(db.get_by_field('*', 'username', form.username.data)[0])

        if user.is_none():
            return redirect(url_for('login'))
        elif not user.check_password(form.password.data):
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
    db = MySQLUser()

    if form.validate_on_submit():
        user = User()
        user.set_password(form.password.data)
        db.insert_field(form.username.data, form.email.data, user.password_hash)
        return redirect(url_for('login'))
    return render_template('register.html', form=form)


@app.route("/add_note", methods=['GET', 'POST'])
@login_required
def add_note():
    form = NoteForm()
    db = MySQLNotes()
    if form.validate_on_submit():
        db.insert_field(current_user.get_id(), form.title.data, form.body.data)
        return redirect(url_for('index'))
    return render_template("add.html", form=form)


@app.route("/my_note/<id>", methods=['GET', 'POST'])
@login_required
def my_note(id):
    form = NoteForm()
    db = MySQLNotes()
    note = db.get_by_field('*', 'id', id)

    if form.is_submitted() and 'save' in request.form:
        db.update_field(id, form.title.data, form.body.data)
        return redirect(url_for('index'))
    elif form.is_submitted() and 'delete' in request.form:
        db.delete_field(id)
        return redirect(url_for('index'))
    form.body.data = note[0][3]
    return render_template('my_note.html', form=form, note=note[0])
