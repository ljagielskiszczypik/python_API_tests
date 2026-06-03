from utils.client_api import Api
import pytest

@pytest.fixture(scope="module")
def apis():
    return Api()

def test_get_users(apis):
    response = apis.get("users")
    assert response.status_code == 200
    assert len(response.json()) > 0
