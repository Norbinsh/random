from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
import os
# from urllib.parse import quote_plus


# Session Management with the LoginManager class
login_manager = LoginManager()
login_manager.session_protection = "strong"
login_manager.login_view = "login"

# Configure the Flask app
app = Flask(__name__)
app.config['SECRET_KEY'] = "RandomVeryStrongKeyGoesHere87978asd456asd13a1sd33969sad36sad2514asd789a32sd1" # To be changed before going production
app.config['DEBUG'] = True
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
login_manager.init_app(app)


# Getting the working directory where the SQLite file will be saved
script_dir = os.path.abspath(os.path.dirname(__file__))

"""
Local SQLite for development purposes, will eventually switch to use one of the Relational DBMS' below
"""
# Configure binds connections
db_one_bind = 'sqlite:///' + os.path.join(script_dir, 'bind_one.db')
db_two_bind = 'sqlite:///' + os.path.join(script_dir, 'bind_two.db')
db_three_bind = 'sqlite:///' + os.path.join(script_dir, 'bind_three.db')

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(script_dir, 'sqlist.db')
app.config['SQLALCHEMY_BINDS'] = {'db_one': db_one_bind, 'db_two': db_two_bind, 'db_three': db_three_bind}


# Initialize 'db'
db = SQLAlchemy(app)


from sqlist import models
from sqlist import views

"""
Default MS SQL Driver + pymssql // Windows
"""
# app.config['SQLALCHEMY_DATABASE_URI'] = 'mssql+pymssql://USER:PASSWORD@@INSTANCE_HOST_NAME:1433/DB_ONE'
# app.config['SQLALCHEMY_BINDS'] = { 'SQList_DB_2': 'mssql+pymssql://USER:PASSWORD@INSTANCE_HOST_NAME:1433/DB_TWO',
#                                    'users': 'mssql+pymssql://USER:PASSWORD@INSTANCE_HOST_NAME:1433/DB_THREE' }

"""
Free TDS + pyodbc // Ubuntu
"""
# app.config['SQLALCHEMY_DATABASE_URI'] = 'mssql+pyodbc:///?odbc_connect={0}'.format(
#         quote_plus(
#             'DRIVER={FreeTDS};SERVER=INSTANCE_HOST_NAME;'
#             'DATABASE=DB_ONE;UID=USER;PWD=PASSWORD;port=1433;'
#             'TDS_Version=8.0;'))
# app.config['SQLALCHEMY_BINDS'] = { 'DB_TWO': 'mssql+pyodbc:///?odbc_connect={0}'.format(
#         quote_plus(
#             'DRIVER={FreeTDS};SERVER=INSTANCE_HOST_NAME;'
#             'DATABASE=DB_TWO;UID=USER;PWD=PASSWORD;port=1433;'
#             'TDS_Version=8.0;')), 'DB_THREE': 'mssql+pyodbc:///?odbc_connect={0}'.format(
#         quote_plus(
#             'DRIVER={FreeTDS};SERVER=INSTANCE_HOST_NAME;'
#             'DATABASE=users;UID=USER;PWD=PASSWORD;port=1433;'
#             'TDS_Version=8.0;')),
#
#             'DB_THREE': 'mssql+pyodbc:///?odbc_connect={0}'.format(
#                     quote_plus(
#                         'DRIVER={FreeTDS};SERVER=INSTANCE_HOST_NAME;'
#                         'DATABASE=DB_THREE;UID=USER;PWD=PASSWORD;port=1433;'
#                         'TDS_Version=8.0;'))
# }