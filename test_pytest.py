from fastapi import FastAPI
import math

from masseis import masseis
from esPrimo import is_prime
app = FastAPI()

def test_primera():
    assert masseis(8)==14

from typing import Union

from fastapi import FastAPI


@app.get("/")   
def read_root():
    return {"Hello": "World"}

@app.get("/hello")   
def hello():
    return {"Hello": "FastAPI"}
 
@app.get("/is_prime/{number}")
async def check_if_prime(number: int):
    if is_prime(number):
        return {"number": number, "is_prime": True}
    else:
        return {"number": number, "is_prime": False}


@app.get("/items/{item_id}")
def read_item(item_id: int, q: Union[str, None] = None):
    return {"item_id": item_id, "q": q}
