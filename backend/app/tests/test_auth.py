def test_register(client):
    response = client.post("/auth/register", json={
        "email": "test@example.com",
        "password": "password123"
    })
    assert response.status_code == 200
    data = response.json()
    assert data["email"] == "test@example.com"
    assert data["credits"] == 5


def test_register_duplicate_email(client):
    client.post("/auth/register", json={
        "email": "test@example.com",
        "password": "password123"
    })
    response = client.post("/auth/register", json={
        "email": "test@example.com",
        "password": "password123"
    })
    assert response.status_code == 400


def test_login(client):
    client.post("/auth/register", json={
        "email": "test@example.com",
        "password": "password123"
    })
    response = client.post("/auth/login", json={
        "email": "test@example.com",
        "password": "password123"
    })
    assert response.status_code == 200
    data = response.json()
    assert "access_token" in data


def test_login_wrong_password(client):
    client.post("/auth/register", json={
        "email": "test@example.com",
        "password": "password123"
    })
    response = client.post("/auth/login", json={
        "email": "test@example.com",
        "password": "wrongpassword"
    })
    assert response.status_code == 401