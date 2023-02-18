from flask_login import UserMixin
from project import login
from project import db
from werkzeug.security import generate_password_hash, check_password_hash


class User(UserMixin):
    id = 0
    username = None
    email = None
    remember_me = False
    password_hash = None

    def load(self, id):
        info = db.get_by_field('*', 'user', 'id', int(id))
        self.id = info[0]
        self.username = info[1]
        self.email = info[2]
        self.password_hash = info[3]
        return self

    def set_password(self, password):
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)

    def __repr__(self):
        return '<User {}>'.format(self.username)


@login.user_loader
def load_user(id):
    user = User()
    user.load(int(id))
    return user
