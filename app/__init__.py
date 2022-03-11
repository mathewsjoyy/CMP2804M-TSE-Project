from flask import Flask
from app.config import Config

app = Flask(__name__)
    
def create_app(config_class=Config):
    # Apply all configuration in the config.py file to the app
    app.config.from_object(config_class)
    
    # import 'main' is the blueprint instance we made at start of main.routes files
    from app.main.routes import main
    
    # Need to register our blueprint before we can use it in our actual app
    app.register_blueprint(main)
    
    return app
