#!/usr/bin/env python3
import sys
import os
import pytest
import flask_security
from unittest.mock import MagicMock, patch

workspace = os.environ.get('WORKSPACE')
backend_path = os.path.join(workspace, 'CRM-backend/app')
sys.path.insert(0, backend_path)
print(backend_path)

# Setezi env variables fake INAINTE de import
os.environ.setdefault('MYSQL_HOST', 'localhost')
os.environ.setdefault('MYSQL_USER', 'test')
os.environ.setdefault('MYSQL_PASSWORD', 'test')
os.environ.setdefault('MYSQL_DATABASE', 'test')
os.environ.setdefault('SECRET_KEY', 'test-secret')


from app import app 

@pytest.fixture
def client():
    with patch('mysql.connector.pooling.MySQLConnectionPool', MagicMock()):
        from app import app

    with app.test_client() as client:
        yield client

#login tests for each endpoint
def test_status_endpoint_security_check(client):
    response = client.get("/api/auth/status")
    assert response.status_code == 401

def test_add_stock_endpoint_security_check(client):
    response = client.post("/api/addStock")
    assert response.status_code == 401

def test_remove_stock_endpoint_security_check(client):
    response = client.post("/api/removeStock")
    assert response.status_code == 401

def test_edit_stock_endpoint_security_check(client):
    response = client.post("/api/editStock")
    assert response.status_code == 401

def test_fetch_stock_endpoint_security_check(client):
    response = client.get("/api/fetchStock")
    assert response.status_code == 401

def test_add_client_endpoint_security_check(client):
    response = client.post("/api/addClient")
    assert response.status_code == 401

def test_fetch_clients_endpoint_security_check(client):
    response = client.get("/api/fetchClients")
    assert response.status_code == 401

def test_remove_client_endpoint_security_check(client):
    response = client.post("/api/removeClient")
    assert response.status_code == 401

def test_edit_client_endpoint_security_check(client):
    response = client.post("/api/editClient")
    assert response.status_code == 401

def test_add_history_endpoint_security_check(client):
    response = client.post("/api/addHistory")
    assert response.status_code == 401

def test_fetch_history_endpoint_security_check(client):
    response = client.get("/api/fetchHistory")
    assert response.status_code == 401