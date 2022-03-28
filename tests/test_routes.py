from flask import Flask
import sys
sys.path.append(".")
from app.main.routes import main

# Basic unit test for routes
def test_base_route():
    app = Flask(__name__)
    app.register_blueprint(main, url_prefix='/')
    
    client = app.test_client()
    
    response = client.get('/')
    
    assert response.status_code == 200
