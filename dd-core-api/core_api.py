#!/usr/bin/env python3

from fastapi import FastAPI

# define an instance of the fastapi app class
dd_api = FastAPI()


@dd_api.get("/")
async def api_root():
    return {"msg": "Hello from Disconnected Dev API!"}
