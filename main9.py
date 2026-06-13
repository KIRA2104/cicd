# pyrefly: ignore [missing-import]
from fastapi import FastAPI
from pydantic import BaseModel


class Student(BaseModel):
    name: str
    age: int
    semester: str


app = FastAPI()


@app.post("/create_student")
def create_student(student: Student):
    return {"message": "Student created successfully", "student": student}
