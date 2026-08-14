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


def test_credit_deduction(client):
    token = get_auth_token(client)
    
    # Save 5 times
    for i in range(5):
        response = client.post("/api/content/save", json={
            "prompt": f"Topic {i}",
            "content_type": "blog",
            "tone": "professional",
            "generated_content": f"Content {i}",
            "word_count": 10
        }, headers={"Authorization": f"Bearer {token}"})
        assert response.status_code == 200
    
    # 6th time should fail
    response = client.post("/api/content/save", json={
        "prompt": "Topic 6",
        "content_type": "blog",
        "tone": "professional",
        "generated_content": "Content 6",
        "word_count": 10
    }, headers={"Authorization": f"Bearer {token}"})
    assert response.status_code == 403


def test_get_credits(client):
    token = get_auth_token(client)
    response = client.get("/api/content/credits", headers={
        "Authorization": f"Bearer {token}"
    })
    assert response.status_code == 200
    data = response.json()
    assert data["credits"] == 5
    assert data["max_credits"] == 5