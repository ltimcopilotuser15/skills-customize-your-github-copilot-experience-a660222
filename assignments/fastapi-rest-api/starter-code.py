# Starter code for FastAPI REST API assignment

from fastapi import FastAPI
from typing import List

app = FastAPI()

items = []

@app.get("/hello")
def read_hello():
    return {"message": "Hello, world!"}

@app.get("/items")
def get_items():
    return {"items": items}

# Add more endpoints for POST, PUT, DELETE as you build your solution!
