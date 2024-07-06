#!/usr/bin/env python3

from fastapi.testclient import TestClient

from core_api import dd_api

client = TestClient(dd_api)


def test_api_root():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"msg": "Hello from Disconnected Dev API!"}

#################### blog endpoints ####################


def test_blog_list():
    response = client.get("/blogs/")
    assert response.status_code == 200
    assert response.json() == {"msg": "Will return a list of blog entries"}


def test_new_blog_post():
    response = client.post("/blogs/new_post/")
    assert response.status_code == 201
    assert response.json() == {"msg": "Create new draft blog post"}


def test_update_blog_post():
    response = client.put("/blogs/update_post/0")
    assert response.status_code == 200
    assert response.json() == {"msg": "Create new draft blog post"}


def test_publish_blog_post():
    response = client.put("/blogs/publish/1001")
    assert response.status_code == 200
    assert response.json() == {
        "msg": "Your post titled:###, has been published"}


def test_users_blog_posts():
    response = client.get("/blogs/users_blogs/600")
    assert response.status_code == 200
    assert response.json() == {"msg": "list of users blog posts"}


def test_blog_post():
    response = client.get("/blogs/post/1001")
    assert response.status_code == 302
    assert response.json() == {"msg": "Will return a specific blog entry"}


def test_blog_remove():
    response = client.delete("/blogs/remove/1001")
    assert response.status_code == 200
    assert response.json() == {"msg": "Blog post deleted from the database!"}

#################### user endpoints ####################


def test_user_add():
    response = client.post("/users/add/")
    assert response.status_code == 200
    assert response.json() == {
        "msg": "The user has been added to the database"}


def test_user_update():
    response = client.put("/users/update/600")
    assert response.status_code == 200
    assert response.json() == {"msg": "The user has been updated"}


def test_user_update_nonexistent():
    response = client.put("/users/update/100")
    assert response.status_code == 404
    assert response.json() == {"detail": "User not found!"}


def user_remove():
    response = client.delete("/users/remove/600")
    assert response.status_code == 200
    assert response.json() == {
        "msg": "The user has been removed from the database"}


def test_user_remove_nonexistent():
    response = client.delete("/users/remove/100")
    assert response.status_code == 404
    assert response.json() == {"detail": "Unable to remove, user not found!"}
