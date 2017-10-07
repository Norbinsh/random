from sqlist import app, db
from flask_script import Manager

# Flask-script manager to add some command line control
manager = Manager(app)

if __name__ == '__main__':
    manager.run()
