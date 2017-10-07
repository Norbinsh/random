from sqlist import db
from flask_login import UserMixin
from werkzeug.security import check_password_hash, generate_password_hash


class Employeesa(db.Model):
    __bind_key__ = 'db_one'
    __tablename__ = 'employeesa'
    EmployeeId = db.Column(db.Integer, primary_key=True)
    FirstName = db.Column(db.String(50))
    LastName = db.Column(db.String(50))
    HireDate = db.Column(db.DateTime)

    def __repr__(self):
        return "{} {} {} {}".format(self.EmployeeId, self.FirstName, self.LastName, self.HireDate)


class Employeesb(db.Model):
    __bind_key__ = 'db_two'
    __tablename__ = 'employeesb'
    EmployeeId = db.Column(db.Integer, primary_key=True)
    FirstName = db.Column(db.String(50))
    LastName = db.Column(db.String(50))
    HireDate = db.Column(db.DateTime)

    def __repr__(self):
        return "{} {} {} {}".format(self.EmployeeId, self.FirstName, self.LastName, self.HireDate)


class Employeesc(db.Model):
    __bind_key__ = 'db_three'
    __tablename__ = 'employeesc'
    EmployeeId = db.Column(db.Integer, primary_key=True)
    FirstName = db.Column(db.String(50))
    LastName = db.Column(db.String(50))
    HireDate = db.Column(db.DateTime)

    def __repr__(self):
        return "{} {} {} {}".format(self.EmployeeId, self.FirstName, self.LastName, self.HireDate)


class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(28), unique=True)
    email = db.Column(db.String(120), unique=True)
    password_hash_value = db.Column(db.String)

    @property
    def password(self):
        raise AttributeError('read only field (password)')

    @password.setter
    def password(self, password):
        self.password_hash_value = generate_password_hash(password)

    def check_password(self, password):
        try:
            return check_password_hash(self.password_hash_value, password)
        except AttributeError as e:
            pass # Should alert here! Password is NULL for the user in the DB.

    @staticmethod
    def get_by_username(username):
        return User.query.filter_by(username=username).first()

    def __repr__(self):
        return "{0}".format(self.username)









