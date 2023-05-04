from fastapi import FastAPI
import math

from masseis import masseis
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

@app.get("/IsPrime")   
def esPrimo(numero):
    if numero < 2:
        return "False"
    for i in range(2, numero):
        if numero % i == 0:
            return "False"
    return "True"



@app.get("/items/{item_id}")
def read_item(item_id: int, q: Union[str, None] = None):
    return {"item_id": item_id, "q": q}
