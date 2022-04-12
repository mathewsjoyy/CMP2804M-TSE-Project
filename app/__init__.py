from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from app.config import Config

app = Flask(__name__)

db = SQLAlchemy()
    
def create_app(config_class=Config):
    # Apply all configuration in the config.py file to the app
    app.config.from_object(config_class)
    
    # Pass in app for our extensions above this class
    db.init_app(app)
    
    # import 'main' is the blueprint instance we made at start of main.routes files
    from app.main.routes import main
    from app.errors.handlers import errors
    
    # Need to register our blueprint before we can use it in our actual app
    app.register_blueprint(main)
    app.register_blueprint(errors)
    
    return app
