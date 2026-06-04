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

def test_update_user(apis, get_payload):
    user_data = get_payload[1]
    response = apis.put(endpoint="users/1", data=user_data)
    assert response.status_code == 200
    assert response.json()['name'] == 'Piotr Nowak'
    assert response.json()['email'] == 'piotr.nowak@example.com'
    assert response.json()['username'] == 'pnowak'
    assert response.json()['address']['city'] == 'Krakow'
    assert response.json()['company']['catchPhrase'] == 'Scalable cloud solutions for everyone'

def test_patch_user(apis, get_payload):
    user_data = get_payload[2]
    response = apis.patch(endpoint="users/1", data=user_data)
    assert response.status_code == 200
    assert response.json()['name'] == 'Marek Zielinski'
    assert response.json()['email'] == 'marek.zielinski@example.com'
    assert response.json()['address']['city'] == 'Poznan'

def test_delete_user(apis):
    response = apis.get("users/1")
    assert response.status_code == 200