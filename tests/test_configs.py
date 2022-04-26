import pytest
import os
from app import create_app

def test_testing_config():
    """
    Given a app object, test that the testing configuration is set
    """
    app = create_app()
    assert app.config['DEBUG']
    assert app.config['TESTING']
    assert app.config['SQLALCHEMY_DATABASE_URI'] == os.environ.get(
        'POSTGRES_URI_LOCAL')

@pytest.mark.skip(reason="Not currently in production")
def test_prod_config():
    """
    Given a app object, test that the production configuration is set
    """
    app = create_app()
    assert not app.config['DEBUG']
    assert not app.config['TESTING']
    assert app.config['SQLALCHEMY_DATABASE_URI'] == os.environ.get(
        'POSTGRES_URI_PROD')