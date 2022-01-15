from fastapi import FastAPI
from pydantic import BaseModel
from typing import Optional


class Item(BaseModel):
    name: str
    consent: Optional[str] = None
    age: int
    tax: Optional[int] = None


app = FastAPI()


@app.get("/items")
def function_one():
    return {"item_id": "called without query parameters"}


@app.get("/items/{id}")
def function_two(id : int):
    return {"item_id" : id}


@app.post("/items/")
def function_three(item: Item):
    return {"result": item}


devesh added this line


