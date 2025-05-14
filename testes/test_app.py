from http import HTTPStatus


def test_created_user(client):
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
