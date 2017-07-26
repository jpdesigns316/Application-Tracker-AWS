from flask import Flask, render_template, request, make_response, redirect, \
    url_for, session, flash
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models import Base, Application, Suggestions
from controllers import *
from functools import wraps
import os

import random
import string

from oauth2client.client import flow_from_clientsecrets
from oauth2client.client import FlowExchangeError
import httplib2
import json
import requests
from flask import session as login_session

from views import *

app = Flask(__name__, template_folder='templates') 
app.config.from_object('config')
app.secret_key = app.config['SECRET_KEY']

# Register Flask Blueprints
engine = create_engine(app.config['SQLALCHEMY_DATABASE_URI'])
admin = app.config['USERNAME']
password = app.config['PASSWORD']
Base.metadata.bind = engine

DBSession = sessionmaker(bind=engine)
session = DBSession()

app.register_blueprint(apply_blueprint, url_prefix='/app')
app.register_blueprint(suggest_blueprint, url_prefix='/suggest')


@app.route('/')
def home():
    return redirect(url_for('app.home'))


# route for handling the login page logic



if __name__ == '__main__':
    app.run(port=6969)
