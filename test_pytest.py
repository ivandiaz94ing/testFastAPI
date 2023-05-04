from fastapi import FastAPI
import math

from masseis import masseis
app = FastAPI()

def test_primera():
    assert masseis(8)==14