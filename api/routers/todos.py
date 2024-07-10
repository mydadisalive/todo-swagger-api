from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from typing import Optional, List

router = APIRouter()

# Base model without ID, for creating new todos
class TodoCreate(BaseModel):
    title: str
    description: Optional[str] = None
    completed: bool = False

# Full Todo model including ID, for response purposes
class Todo(TodoCreate):
    id: int

todos = [
    {"id": 1, "title": "Buy groceries", "description": "Milk, Bread, Cheese", "completed": False},
    {"id": 2, "title": "Read a book", "description": "The Catcher in the Rye", "completed": False},
]

@router.get("/todos", response_model=List[Todo])
async def get_todos():
    return todos

@router.get("/todos/{todo_id}", response_model=Todo)
async def get_todo(todo_id: int):
    for todo in todos:
        if todo["id"] == todo_id:
            return todo
    raise HTTPException(status_code=404, detail="Todo not found")

@router.post("/todos", response_model=Todo)
async def create_todo(todo: TodoCreate):
    new_id = max(todo['id'] for todo in todos) + 1 if todos else 1
    new_todo = todo.model_dump()  # Changed from dict() to model_dump()
    new_todo["id"] = new_id
    todos.append(new_todo)
    return new_todo

@router.put("/todos/{todo_id}", response_model=Todo)
async def update_todo(todo_id: int, updated_todo: Todo):
    for index, todo in enumerate(todos):
        if todo["id"] == todo_id:
            todos[index] = updated_todo.model_dump()  # Changed from dict() to model_dump()
            return updated_todo
    raise HTTPException(status_code=404, detail="Todo not found")

@router.delete("/todos/{todo_id}", response_model=Todo)
async def delete_todo(todo_id: int):
    for index, todo in enumerate(todos):
        if todo["id"] == todo_id:
            deleted_todo = todos.pop(index)
            return deleted_todo
    raise HTTPException(status_code=404, detail="Todo not found")
