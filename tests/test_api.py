from utils.client_api import Api
import pytest

@pytest.fixture(scope="module")
def apis():
    return Api()

def test_get_users(apis):
    response = apis.get("users")
    assert response.status_code == 200
    assert len(response.json()) > 0

def test_get_specific_user(apis):
    response = apis.get(endpoint=f"users/1")
    assert response.status_code == 200
    assert response.json()['name'] == 'Leanne Graham'
    assert response.json()['email'] == 'Sincere@april.biz'
    assert response.json()['username'] == 'Bret'
    assert response.json()['address']['city'] == 'Gwenborough'

def test_create_user(apis, get_payload):
    user_data = get_payload[0]
    response = apis.post(endpoint="users", data=user_data)
    assert response.status_code == 201
    assert response.json()['name'] == 'Anna Kowalska'
    assert response.json()['email'] == 'anna.kowalska@example.com'
    assert response.json()['username'] == 'ankow'
    assert response.json()['address']['city'] == 'Wroclaw'
