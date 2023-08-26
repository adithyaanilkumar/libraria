import os
from dotenv import load_dotenv
basedir = os.path.abspath(os.path.dirname(__file__))




class DevelopmentConfig():
    DEBUG = True
    DEVELOPMENT = True
    CSRF_ENABLED = False
    SECRET_KEY = 'ihatecrypto'
    SQLALCHEMY_DATABASE_URI = os.getenv('DATABASE_URL')

