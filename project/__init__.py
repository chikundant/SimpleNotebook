from flask import Flask
from config import Config
from flask_login import LoginManager
from project.db import MySQL

app = Flask(__name__)
app.config.from_object(Config)
db = MySQL()
login = LoginManager(app)
login.login_view = 'login'

app.debug = True

from project import routes
