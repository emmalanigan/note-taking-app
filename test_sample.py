

import pytest
from app import app

@pytest.fixture
def client():
    with app.test_client() as client:
        yield client


def test_index_page(client):
    response = client.get('/')
    assert response.status_code == 200

    assert b'<title>Note taking app</title>' in response.data
    assert b'This is the Index page' in response.data