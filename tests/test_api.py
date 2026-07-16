from fastapi.testclient import TestClient

from app.main import app

client = TestClient(app)


def test_health_endpoint_returns_ok():
    response = client.get("/health")
    assert response.status_code == 200
    assert response.json() == {"status": "ok"}


def test_version_endpoint_returns_version():
    response = client.get("/version")
    assert response.status_code == 200
    assert response.json()["version"] == "2.0.0"


def test_products_endpoint_returns_catalog():
    response = client.get("/products")
    assert response.status_code == 200
    assert len(response.json()) == 3


def test_products_count_endpoint_returns_count():
    response = client.get("/products/count")
    assert response.status_code == 200
    assert response.json() == {"count": 3}


def test_missing_product_returns_404():
    response = client.get("/products/999")
    assert response.status_code == 404
    assert response.json()["detail"] == "Product not found"
