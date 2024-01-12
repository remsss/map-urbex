from flask import url_for, Flask, request, render_template, redirect, make_response
from datetime import datetime, timedelta
from argon2 import PasswordHasher
from uuid import uuid1, uuid3
from random import randint
from Utils.validation_email import envoyer_email_verification #Utils is a folder in the root of the project
from Utils.utils import add_addresse_to_db, create_6_number_string
from Utils.database import DataBase
import pymysql

ph = PasswordHasher()
db = DataBase(user='root', password='LeMdPPourROOTTT', host='127.0.0.1', port=3306, database='map-urbex')
db.connection()

app = Flask(__name__)

@app.route('/root')
def root():
    return render_template('root.html')

@app.route('/')
def home():
    return render_template('index.html')


@app.route('/map')
def map():
    return render_template('map.html')






if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port='20079')