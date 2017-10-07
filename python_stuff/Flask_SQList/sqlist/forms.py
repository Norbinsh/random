from flask_wtf import FlaskForm
from wtforms.fields import StringField, PasswordField, BooleanField, SubmitField, SelectField, RadioField
from wtforms.validators import DataRequired, Length, Email, Regexp, EqualTo, ValidationError
from sqlist.models import User
from sqlist import app


class SignUp(FlaskForm):
    username = StringField('Username', validators=[DataRequired(), Length(min=4, max=25), Regexp('^[A-Za-z0-9]{3,}$',
                            message='Letters and numbers only')])
    email = StringField('Email', [DataRequired(), Length(min=6, max=25), Email()])
    password = PasswordField('Password', validators=[DataRequired(), EqualTo('password2',
                                                                             message="Passwords must match.")])
    password2 = PasswordField('Confirm Password', validators=[DataRequired()])

    def validate_email(self, email_address_field):
        if User.query.filter_by(email=email_address_field.data).first():
            raise ValidationError('Email address already in use.')

    def validate_username(self, username_field):
        if User.query.filter_by(username=username_field.data).first():
            raise ValidationError('Username is already taken.')


class LoginForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    remember_me = BooleanField('Stay logged in')
    submit = SubmitField(label='Submit')


class CncAction(FlaskForm):
    choose_action = RadioField(label="", validators=[DataRequired()], choices=[("search_record", "Search Record"),
                    ("delete_record", "Delete Record"),("add_record", "Add Record")])
    submit = SubmitField()


class SelectDB(FlaskForm):
    db_name = SelectField('',validators=[DataRequired()], choices=[(x,x) for x in app.config['SQLALCHEMY_BINDS']])
    submit = SubmitField()


class SelectTB(FlaskForm):
    tb_name = SelectField('', coerce=str, validators=[DataRequired()])
    id_lookup = StringField('ID # (Optional)', validators=[Length(min=0, max=8), Regexp('^[0-9]{0,8}$',
                                                                                       message='Numbers only')])
    submit = SubmitField()


