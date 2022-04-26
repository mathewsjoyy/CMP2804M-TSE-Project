import pytest
from app import create_app

# Pytest fixture to create a Flask application and basic configuration
@pytest.fixture(scope='module')
def test_client():
    flask_app = create_app()
    
    # Create a test client using the flask application configured for testing
    with flask_app.test_client() as testing_client:
        yield testing_client    # This is where the testing happens

def test_base_route(test_client):
    """
    Given a Flask application
    When the '/' route is requested (GET)
    Then a status code of 200 is returned
    """
    response = test_client.get('/')
    
    assert response.status_code == 200

def test_reviews_route(test_client):
    """
    Given a Flask application
    When the '/reviews' route is requested (GET)
    Then a status code of 200 is returned
    """
    response = test_client.get('/reviews')
    
    assert response.status_code == 200

def test_404_error_route(test_client):
    """
    Given a Flask application
    When a invalid route is requested (GET)
    Then a status code of 404 is returned
    """
    response = test_client.get('/does_not_exist')

    assert response.status_code == 404
