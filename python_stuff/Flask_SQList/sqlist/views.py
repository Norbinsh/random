import importlib
from flask import render_template, url_for, request, redirect, flash
from sqlist import app, db, login_manager
from sqlist.models import User
from sqlist.forms import SignUp, LoginForm, CncAction, SelectDB, SelectTB
from flask_login import login_user, logout_user, current_user, login_required
from sqlist.util import util_list_tables
from sqlalchemy import desc

@login_manager.user_loader
def load_user(userid):
    return User.query.get(int(userid))


@app.route('/')
@app.route('/index')
def index():
    if current_user.is_authenticated:
        return render_template('index.html', customtitle="Welcome to SQList Index Page")
    else:
        return render_template('anonymous_index.html', customtitle="Anonymous! You are not logged in")


@app.route('/signup', methods=['POST', 'GET'])
def signup():
    form = SignUp()
    if form.validate_on_submit():
        user = User(username=form.username.data, email=form.email.data, password=form.password.data)
        db.session.add(user)
        db.session.commit()
        flash('Registration completed! Please log in below')
        return redirect(url_for('login'))
    return render_template('signup.html', form=form, customtitle="SQList Signup Form")


@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        user = User.get_by_username(form.username.data)
        if user is not None and user.check_password(form.password.data):
            login_user(user, form.remember_me.data)
            flash("Welcome {}!".format(user.username))
            return redirect(request.args.get('next') or url_for('index'))
        flash('Username or password incorrect')
    return render_template('login.html', form=form, customtitle="SQList Login Form")


@app.route('/logout')
@login_required
def logout():
    logout_user()
    flash("Successfully logged out")
    return redirect('index')


@app.route('/cnc', methods=['POST', 'GET'])
@login_required
def cnc():
    form = CncAction()
    if form.validate_on_submit():
        if form.choose_action.data == "search_record":
            return redirect(url_for('search_record'))
        elif form.choose_action.data == "delete_record":
            return redirect(url_for('delete_record'))
        else:
            return redirect(url_for('add_record'))
    return render_template('cnc.html', customtitle="SQList Command And Conquer", form=form)


@app.route('/cnc/search_record', methods=['POST', 'GET'])
@login_required
def search_record():
    form = SelectDB()
    if form.validate_on_submit():
        db_name = form.db_name.data
        return redirect(url_for('list_tables', passed_database_name=db_name))
    return render_template('search_record.html', customtitle="SQList Search Page", form=form)


@app.route('/cnc/search_record/<passed_database_name>', methods=['GET', 'POST'])
@login_required
def list_tables(passed_database_name):
    form = SelectTB()
    form.tb_name.choices = util_list_tables(passed_database_name)
    if form.validate_on_submit():
        return redirect(url_for('display_records', passed_database_name=passed_database_name,
                                display_records_for=form.tb_name.data, id_lookup=form.id_lookup.data))
    return render_template('tables.html', form=form, no_tables=True if len(form.tb_name.choices) == 0 else False,
                           passed_database_name=passed_database_name)


@app.route('/cnc/search_record/<passed_database_name>/<display_records_for>', methods=['POST', 'GET'])
@login_required
def display_records(passed_database_name, display_records_for):
    id_lookup = request.args.get('id_lookup')

    xapital = display_records_for.title()
    MyRClass = getattr(importlib.import_module("sqlist.models"), xapital)
    xinstance = MyRClass()
    if len(id_lookup) == 0:
        no_id_list = xinstance.query.order_by(desc('HireDate')).limit(5).all()
    else:
        no_id_list = xinstance.query.filter_by(EmployeeId=id_lookup).first()
        print(no_id_list)

    return render_template('display_records.html', display_record_database_name=passed_database_name,
                           display_records_for=display_records_for,id_lookup=id_lookup, no_id_list=no_id_list)


@app.errorhandler(404)
def page_does_not_exist(error_number):
    return render_template('404.html', customtitle="Page Not Found"), 400


@app.errorhandler(500)
def internal_server_error(error_number):
    return render_template('500.html', customtitle="Internal Server Error"), 500
