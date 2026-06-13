# pyrefly: ignore [missing-import]
from fastapi import FastAPI
from pydantic import BaseModel


class Address(BaseModel):
    street: str
    city: str
    state: str


class user(BaseModel):
    name: str
    age: int
    email: str
    address: Address


app = FastAPI()


@app.get("/create_user")
def create_user(name: str, age: int, email: str, street: str, city: str, state: str):
    addr = Address(street=street, city=city, state=state)
    u = user(name=name, age=age, email=email, address=addr)
    return u

