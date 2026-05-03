from app import app, get_message


def test_home_status_code():
    client = app.test_client()
    response = client.get("/")
    assert response.status_code == 200


def test_home_message():
    client = app.test_client()
    response = client.get("/")
    assert response.data.decode("utf-8") == "Hello, Continuous Deployment v2!"


def test_health_status_code():
    client = app.test_client()
    response = client.get("/health")
    assert response.status_code == 200


def test_get_message():
    assert get_message() == "Hello, Continuous Deployment v2!"
