def get_auth_token(client):
    client.post("/auth/register", json={
        "email": "test@example.com",
        "password": "password123"
    })
    response = client.post("/auth/login", json={
        "email": "test@example.com",
        "password": "password123"
    })
    return response.json()["access_token"]


def test_save_content(client):
    token = get_auth_token(client)
    response = client.post("/api/content/save", json={
        "prompt": "Write about AI",
        "content_type": "blog",
        "tone": "professional",
        "generated_content": "AI is the future...",
        "word_count": 10
    }, headers={"Authorization": f"Bearer {token}"})
    
    assert response.status_code == 200
    data = response.json()
    assert data["credits_remaining"] == 4


def test_get_history(client):
    token = get_auth_token(client)
    client.post("/api/content/save", json={
        "prompt": "Write about AI",
        "content_type": "blog",
        "tone": "professional",
        "generated_content": "AI is the future...",
        "word_count": 10
    }, headers={"Authorization": f"Bearer {token}"})
    
    response = client.get("/api/content/history", headers={
        "Authorization": f"Bearer {token}"
    })
    assert response.status_code == 200
    data = response.json()
    assert len(data) == 1


def test_save_without_auth(client):
    response = client.post("/api/content/save", json={
        "prompt": "Write about AI",
        "content_type": "blog",
        "tone": "professional",
        "generated_content": "AI is the future...",
        "word_count": 10
    })
    assert response.status_code == 401