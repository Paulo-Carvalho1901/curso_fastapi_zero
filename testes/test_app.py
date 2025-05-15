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

def test_read_users(client):
    response = client.get('/users/')

    assert response.status_code == HTTPStatus.OK
    assert response.json() == {'users':[
        {
            'username': 'testeusername',
            'email':  'test@teste.com',
            'id': 1
        }
    ]}

def test_update_user(client):
    response = client.put(
        '/users/1',
        json={
            'password': '1236',
            'username': 'testeusername2',
            'email':  'test@teste.com',
            'id': 1
        }
    )
    assert response.json() == {
        'username': 'testeusername2',
        'email':  'test@teste.com',
        'id': 1
    }