# pyrefly: ignore [missing-import]
from fastapi import FastAPI

app = FastAPI()


@app.get("/create_user")
def create_user(name: str, age: int):
    return {"message": "User created successfully", "user": {"name": name, "age": age}}
