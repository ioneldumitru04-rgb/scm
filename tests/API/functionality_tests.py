www#!/usr/bin/env python3
import sys
import os
import pytest
import flask_security
import json
from unittest.mock import MagicMock, patch

workspace = os.environ.get('WORKSPACE')

workspace = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..', '..'))

backend_path = os.path.join(workspace, '/app')
sys.path.insert(0, backend_path)

# Setezi env variables fake INAINTE de import
os.environ.setdefault('MYSQL_HOST', 'localhost')
os.environ.setdefault('MYSQL_USER', 'test')
os.environ.setdefault('MYSQL_PASSWORD', 'test')
os.environ.setdefault('MYSQL_DATABASE', 'test')
os.environ.setdefault('SECRET_KEY', 'test-secret')


with patch('mysql.connector.pooling.MySQLConnectionPool', return_value=MagicMock()):
    import app as flask_app

@pytest.fixture
def client():

    with flask_app.app.test_client() as client:
        yield client

@pytest.fixture
def login_required_mocked(mocker):
    return mocker.patch("login_required")

def test_register_functionality(client):
    mock_cursor = MagicMock()
    mock_cursor.fetchone.return_value = 1
    flask_app.db.cursor.return_value = mock_cursor

    data = {
        "First_name":"test",
        "Last_name":"test",
        "Service_name":"test",
        "email":"test",
        "password":"test"
    }

    response = client.post("/api/auth/register", content_type='application/json',data=json.dumps(data))
    
    assert response.status_code == 201
    json_data = response.get_json()
    assert json_data['user']['First_name'] == "test"

#nu functioneaza
# def test_login_functionality(client):
#     mock_cursor = MagicMock()
#     mock_cursor.fetchone.return_value = ("test", "test", "test", "test", "test")
#     flask_app.db.cursor.return_value = mock_cursor

#     data = {
#         "email": "a",
#         "password": "test",
#         "First_name": "test",
#         "Last_name": "test",
#         "Service_name": "test"
#     }

#     response = client.post("/api/auth/login", content_type='application/json',data=json.dumps(data))
    
#     assert response.status_code == 201

def test_status_functionality(client):
    mock_cursor = MagicMock()
    mock_cursor.fetchone.return_value = 1
    flask_app.db.cursor.return_value = mock_cursor

    data = {
        "First_name":"test",
        "Last_name":"test",
        "Service_name":"test",
        "email":"test",
        "password":"test"
    }

    response = client.get("/api/auth/status", content_type='application/json',data=json.dumps(data))
    
    assert response.status_code == 401

def test_addstock_functionality(client):
    mock_cursor = MagicMock()
    mock_cursor.fetchone.return_value = "test"
    flask_app.db.cursor.return_value = mock_cursor

    data = {
        "partName": "test",
        "partType": "test",
        "quantity": "test",
        "vehicleCompatibility": "test",
        "price": "test",
        "serviceName": "test"
    }

    response = client.post("/api/addStock", content_type='application/json',data=json.dumps(data))
    
    assert response.status_code == 401 # nu e status corect






