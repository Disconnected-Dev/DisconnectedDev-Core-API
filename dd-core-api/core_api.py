#!/usr/bin/env python3

from fastapi import FastAPI, status, HTTPException, Depends
from pydantic import BaseModel


class Blog(BaseModel):
    bID: int
    bTitle: str
    bText: str
    bFullText: str
    bCount: int
    bCreated: str


class User(BaseModel):
    uID: int
    uName: str
    uPassword: str
    uEmail: str
    uSignup: str
    uLastLogin: str
    uDissabled: bool


# define an instance of the fastapi app class
dd_api = FastAPI()


@dd_api.get("/")
async def api_root():
    return {"msg": "Hello from Disconnected Dev API!"}

#################### login endpoints ####################


@dd_api.post("/login/")
async def api_login():
    return {"msg": "Endpoint to log you in"}


@dd_api.post("/login/change_password/{username}")
async def api_chgpass(username: str):
    if username != str("testuser"):
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="User not found!")
    return {"msg": "Your Password has been changed"}


@dd_api.post("/login/forgotten_password/{username}")
async def api_fgtpass(username: str):
    if username != str("testuser"):
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="User not found!")
    return {"msg": "An email with a reset link has been sent to $email"}

#################### blog endpoints ####################


@dd_api.get("/blogs/")
async def blog_list():
    # ommit draft blogs
    return {"msg": "Will return a list of blog entries"}


@dd_api.post("/blogs/new_post/", status_code=status.HTTP_201_CREATED)
async def new_blog_post():
    return {"msg": "Create new draft blog post"}


@dd_api.put("/blogs/update_post/{blog_id}")
async def update_blog_post(blog_id: int):
    return {"msg": "Create new draft blog post"}


@dd_api.put("/blogs/publish/{blog_id}", status_code=status.HTTP_200_OK)
async def publish_blog_post(blog_id: int):
    return {"msg": "Your post titled:###, has been published"}


@dd_api.get("/blogs/users_blogs/{user_id}")
async def users_blog_posts(user_id: int):
    return {"msg": "list of users blog posts"}


@dd_api.get("/blogs/post/{blog_id}", status_code=status.HTTP_302_FOUND)
async def blog_post(blog_id: int):
    # add user presence check for draft blog
    return {"msg": "Will return a specific blog entry"}


@dd_api.delete("/blogs/remove/{blog_id}")
async def blog_remove(blog_id: int):
    return {"msg": "Blog post deleted from the database!"}

#################### user endpoints ####################


@dd_api.post("/users/add/")
async def user_add():
    return {"msg": "The user has been added to the database"}


@dd_api.put("/users/update/{user_id}", status_code=status.HTTP_200_OK)
async def user_update(user_id: int):
    if user_id != int("600"):
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="User not found!")
    return {"msg": "The user has been updated"}


@dd_api.delete("/users/remove/{user_id}")
async def user_remove(user_id: int):
    if user_id != int("600"):
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="Unable to remove, user not found!")
    return {"msg": "The user has been removed from the database"}
