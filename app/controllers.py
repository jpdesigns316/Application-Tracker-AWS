from flask import Flask
from sqlalchemy import create_engine, desc
from sqlalchemy.orm import sessionmaker
import datetime
from models import *

app = Flask(__name__)
app.config.from_object('config')
app.secret_key = app.config['SECRET_KEY']


def load_engine():
    engine = create_engine(app.config['SQLALCHEMY_DATABASE_URI'])
    return engine


engine = load_engine()
Base.metadata.bind = engine

DBSession = sessionmaker(bind=engine)
session = DBSession()


def get_applications(order):
    if order == 'desc':
        return session.query(Application).order_by(desc(Application.date_apply)).all()
    else:
        return session.query(Application).order_by(Application.date_apply).all()


def sort_applications_by_company(order):
    if order == 'desc':
        return session.query(Application).order_by(desc(Application.company_name)).all()
    else:
        return session.query(Application).order_by(Application.company_name).all()


def get_application(id):
    return session.query(Application).filter_by(id=id).one()


def past_week_applications():
    today = datetime.date.today()
    week = today.weekday()
    start_delta = datetime.timedelta(weeks=1)
    last_week = today - start_delta
    qry = session.query(Application).filter(Application.date_apply >= str(last_week)).order_by(Application.date_apply)
    return qry



def search_applications(start_date, end_date):
    qry = session.query(Application).filter(Application.date_apply <= end_date).\
        filter(Application.date_apply >= start_date)
    return qry



