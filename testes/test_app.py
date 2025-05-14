from http import HTTPStatus
from fastapi import status
from fastapi.testclient import TestClient

from main import app


def test_created_user():
    client = TestClient(app)

    response = client.post(
        '/users/', 
        json={
            'username': 'testeusername',
            'password': 'password',
            'email':  'test@teste.com',
        }
    )

    # Voltou o status code correto?
    assert response.status_code == HTTPStatus.CREATED
    # Validação UserPublic

    assert response.json() == {
        'username': 'testeusername',
        'email':  'test@teste.com',
        'id': 1,
    }
