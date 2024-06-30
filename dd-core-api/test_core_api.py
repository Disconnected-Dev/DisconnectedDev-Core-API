#!/usr/bin/env python3

from fastapi.testclient import TestClient

from .core_api import dd_api

client = TestClient(dd_api)


def test_api_root():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"msg": "Hello from Disconnected Dev API!"}
