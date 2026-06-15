# pyright: ignore [reportMissingImports]
from fastapi import FastAPI

# pyright: ignore [reportMissingImports]
from fastapi.responses import FileResponse
from pydantic import BaseModel

app = FastAPI()


@app.get("/")
def get_home():
    return FileResponse("index.html")


todos = []


class Todo(BaseModel):
    id: int
    title: str
    description: str
    completed: bool


@app.post("/todos")
def create_todo(todo: Todo):
    todos.append(todo)
    return {"message": "Todo added", "data": todo}


@app.get("/todos")
def get_todos():
    return todos


@app.get("/todos/{todo_id}")
def get_todo(todo_id: int):
    for todo in todos:
        if todo.id == todo_id:
            return todo
    return {"message": "Todo not found"}


@app.put("/todos/{todo_id}")
def update_todo(todo_id: int, updated_todo: Todo):
    for index, todo in enumerate(todos):
        if todo.id == todo_id:
            todos[index] = updated_todo
            return {"message": "Todo updated", "data": updated_todo}
    return {"message": "Todo not found"}


@app.delete("/todos/{todo_id}")
def delete_todo(todo_id: int):
    for index, todo in enumerate(todos):
        if todo.id == todo_id:
            deleted_todo = todos.pop(index)
            return {"message": "Todo deleted", "data": deleted_todo}
    return {"message": "Todo not found"}
