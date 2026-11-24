import pytest
from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_search_returns_results():
    """Test that /search endpoint returns results for a given username."""
    response = client.get("/search?username=theabbie")
    assert response.status_code == 200
    data = response.json()
    assert data["username"] == "theabbie"
    assert len(data["sites"]) == 3
    # Verify URLs have username substituted
    sites = data["sites"]
    assert sites[0]["name"] == "GitHub"
    assert "theabbie" in sites[0]["url"]
    assert sites[1]["name"] == "Instagram"
    assert "theabbie" in sites[1]["url"]
    assert sites[2]["name"] == "Twitter"
    assert "theabbie" in sites[2]["url"]
