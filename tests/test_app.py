import os
import sys

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "app"))

from app import add, app  # noqa: E402


def client():
    app.config["TESTING"] = True
    return app.test_client()


def test_index_returns_message():
    resp = client().get("/")
    assert resp.status_code == 200
    assert resp.get_json()["message"] == "Hello from CI/CD pipeline v2!"


def test_health():
    resp = client().get("/health")
    assert resp.status_code == 200
    assert resp.get_json() == {"status": "ok"}


def test_add():
    assert add(2, 3) == 5
