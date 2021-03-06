from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, DateField, PasswordField, SelectField, FileField
from wtforms.validators import DataRequired, Required
from controllers import *
import datetime


class LoginForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])


class SearchForm(FlaskForm):
    start_date = DateField('Start Date')
    end_date = DateField('End Date')


class ApplicationAddForm(FlaskForm):
    today = datetime.date.today
    company_name = StringField('Company Name', validators=[DataRequired()])
    date_apply = DateField('Date Applied', validators=[DataRequired(
    )], format='%Y-%m-%d', default=datetime.date(today().year, today().month, today().day))
    position = StringField('Position', validators=[DataRequired()])
    location = StringField('Location', validators=[DataRequired()])
    next_step = StringField('next_step', validators=[DataRequired()])
    contact = StringField('contact', validators=[DataRequired()])
    job_board = StringField('job_board', validators=[DataRequired()])
    notes = TextAreaField('notes', validators=[DataRequired()])


class ApplicationEditForm(FlaskForm):

    today = datetime.date.today

    company_name = StringField('Company Name', validators=[DataRequired()])
    date_apply = DateField('Date Applied', validators=[DataRequired(
    )], format='%Y-%m-%d', default=datetime.date(today().year, today().month, today().day))
    position = StringField('Position', validators=[DataRequired()])
    location = StringField('Location', validators=[DataRequired()])
    next_step = StringField('next_step', validators=[DataRequired()])
    contact = StringField('contact', validators=[DataRequired()])
    job_board = StringField('job_board', validators=[DataRequired()])
    notes = TextAreaField('notes', validators=[DataRequired()])

