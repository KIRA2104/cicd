# pyrefly: ignore [missing-import]
from fastapi import FastAPI

app = FastAPI()


@app.post("/create_user")
def create_user(name: str, age: int, semester: str):
    return {
        "message": "user created",
        "data": {"name": name, "age": age, "semester": semester},
    }
