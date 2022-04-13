import os
from dotenv import load_dotenv, find_dotenv
load_dotenv(find_dotenv())

# Class that holds the configuration for the app
# including the secret key, database configuration, and other
class Config:
    # App secret key (needed to run on heroku)
    SECRET_KEY = str(os.environ.get('SECRET_KEY').encode('utf-8'))
    
    # Database configurations
    uri = ""
    ENV = 'PROD'

    if ENV == 'DEV':    # In development mode, we use the local database / debug mode
        uri = os.environ.get('POSTGRES_URI_LOCAL')
    else:   # In production mode, we use the database (hosted & managed by Heroku)
        uri = os.getenv('POSTGRES_URI_PROD')

    SQLALCHEMY_DATABASE_URI = uri
    SQLALCHEMY_TRACK_MODIFICATIONS = False
