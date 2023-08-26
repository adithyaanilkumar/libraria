from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from config import DevelopmentConfig
import os

app = Flask(__name__)

app.config.from_object(DevelopmentConfig)
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)





@app.route('/heartbeat')
def hear_beat():
    return "Hello From the other side."