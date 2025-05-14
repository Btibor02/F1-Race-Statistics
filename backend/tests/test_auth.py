import pytest
from app import create_app, db
from app.models import User

@pytest.fixture
def client():
    app = create_app()
    app.config['TESTING'] = True
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///:memory:'
    app.config['WTF_CSRF_ENABLED'] = False

    with app.test_client() as client:
        with app.app_context():
            db.create_all()
        yield client

def register(client, username, email, password, confirm):
    return client.post('/register', data={
        'username': username,
        'email': email,
        'password': password,
        'confirm_password': password
    }, follow_redirects=True)

def login(client, username, password):
    return client.post('/login', data={
        'username': username,
        'password': password,
        'submit': True
    }, follow_redirects=True)

def test_register_success(client):
    response = register(client, 'testuser', 'testuser@example.com', 'Password123!', 'Password123!')
    print(response.status_code)
    print(response.data)
    assert b'Congratulations, you are now a registered user!' in response.data

def test_login_success(client):
    register(client, 'testuser', 'testuser@example.com', 'Password123!', 'Password123!')
    response = login(client, 'testuser', 'Password123!')
    assert b'Login successful!' in response.data

def test_login_invalid(client):
    response = login(client, 'nonexistentuser', 'Password123!')
    assert b'Invalid username or password' in response.data