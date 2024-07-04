#!/usr/bin/env python3

from fastapi import FastAPI
from pydantic import basemodel

# define an instance of the fastapi app class
dd_api = FastAPI()


class Blog(BaseModel):
    bID: int
    bTitle: str
    bText: str
    bFullText: str
    bCount: int | none = none
    bCreated: str


@dd_api.get("/")
async def api_root():
    return {"msg": "Hello from Disconnected Dev API!"}

#################### blog endpoints ####################


@dd_api.get("/blogs/")
async def blog_list():
    # ommit draft blogs
    return {"msg": "Will return a list of blog entries"}


@dd_api.post("/blogs/new_post/")
async def new_blog_post():
    return {"msg": "Create new draft blog post"}


@dd_api.put("/blogs/update_post/{blog_id}")
async def update_blog_post():
    return {"msg": "Create new draft blog post"}


@dd_api.put("/blogs/pub_post/{blog_id}")
async def publish_blog_post(blog_id: int):
    return {"msg": "Your post titled:###, has been published"}


@dd_api.get("/blogs/users_posts")
async def users_blog_posts():
    return {"msg": "list of users blog posts"}


@dd_api.get("/blogs/post/{blog_id}")
async def blog_post(blog_id: int):
    # add user presence check for draft blog
    return {"msg": "Will return a specific blog entry"}


@dd_api.delete("/blogs/remove/{blog_id}")
async def blog_remove(blog_id: int):
    return {"msg": "Blog post deleted from the database!"}

#################### user endpoints ####################


@dd_api.put("/users/add/")
async def user_add():
    return {"msg": "The user has been added to the database"}


@dd_api.post("/users/update/{user_id}")
async def user_add(user_id: int):
    return {"msg": "The user has been updated"}


@dd_api.put("/users/remove/{user_id}")
async def user_add(user_id: int):
    return {"msg": "The user has been removed from the database"}
