from fastapi import FastAPI, WebSocket, HTTPException
from api.routers import todos
from pydantic import BaseModel
from typing import Optional, List
import logging

app = FastAPI()

# Initialize logger
logger = logging.getLogger("uvicorn")
logging.basicConfig(level=logging.INFO)

@app.get("/")
async def read_root():
    """
    Root endpoint returning a welcome message.
    """
    logger.info("Root endpoint accessed")
    return {"message": "Welcome to the Todo API!"}

app.include_router(todos.router)

todos = [
    {"id": 1, "title": "Buy groceries", "description": "Milk, Bread, Cheese", "completed": False},
    {"id": 2, "title": "Read a book", "description": "The Catcher in the Rye", "completed": False},
]

@app.websocket("/ws")
async def websocket_endpoint(websocket: WebSocket):
    """
    WebSocket endpoint for real-time todo management commands.
    """
    await websocket.accept()
    try:
        while True:
            data = await websocket.receive_text()
            command_parts = data.split()
            command = command_parts[0]

            if command == "list-todos":
                await websocket.send_text(str(todos))
                logger.info("list-todos command executed")

            elif command == "get-todo":
                if len(command_parts) < 2:
                    await websocket.send_text("Error: Missing todo_id")
                    logger.error("get-todo command failed: Missing todo_id")
                    continue
                try:
                    todo_id = int(command_parts[1])
                    todo = next((todo for todo in todos if todo["id"] == todo_id), None)
                    if todo is None:
                        await websocket.send_text("Error: Todo not found")
                        logger.error(f"get-todo command failed: Todo {todo_id} not found")
                    else:
                        await websocket.send_text(str(todo))
                        logger.info(f"get-todo command executed: Todo {todo_id} retrieved")
                except ValueError:
                    await websocket.send_text("Error: Invalid todo_id")
                    logger.error("get-todo command failed: Invalid todo_id")

            elif command == "create-todo":
                if len(command_parts) < 2:
                    await websocket.send_text("Error: Missing title")
                    logger.error("create-todo command failed: Missing title")
                    continue
                title = command_parts[1]
                description = " ".join(command_parts[2:]) if len(command_parts) > 2 else None
                new_id = max(todo['id'] for todo in todos) + 1 if todos else 1
                new_todo = {"id": new_id, "title": title, "description": description, "completed": False}
                todos.append(new_todo)
                await websocket.send_text(f"Created todo: {new_todo}")
                logger.info(f"create-todo command executed: {new_todo}")

            elif command == "update-todo":
                if len(command_parts) < 3:
                    await websocket.send_text("Error: Missing parameters")
                    logger.error("update-todo command failed: Missing parameters")
                    continue
                try:
                    todo_id = int(command_parts[1])
                    title = command_parts[2]
                    description = " ".join(command_parts[3:]) if len(command_parts) > 3 else None
                    completed = "--completed" in command_parts
                    updated_todo = {"id": todo_id, "title": title, "description": description, "completed": completed}
                    for index, todo in enumerate(todos):
                        if todo["id"] == todo_id:
                            todos[index] = updated_todo
                            await websocket.send_text(f"Updated todo: {updated_todo}")
                            logger.info(f"update-todo command executed: {updated_todo}")
                            break
                    else:
                        await websocket.send_text("Error: Todo not found")
                        logger.error(f"update-todo command failed: Todo {todo_id} not found")
                except ValueError:
                    await websocket.send_text("Error: Invalid todo_id")
                    logger.error("update-todo command failed: Invalid todo_id")

            elif command == "delete-todo":
                if len(command_parts) < 2:
                    await websocket.send_text("Error: Missing todo_id")
                    logger.error("delete-todo command failed: Missing todo_id")
                    continue
                try:
                    todo_id = int(command_parts[1])
                    for index, todo in enumerate(todos):
                        if todo["id"] == todo_id:
                            deleted_todo = todos.pop(index)
                            await websocket.send_text(f"Deleted todo: {deleted_todo}")
                            logger.info(f"delete-todo command executed: {deleted_todo}")
                            break
                    else:
                        await websocket.send_text("Error: Todo not found")
                        logger.error(f"delete-todo command failed: Todo {todo_id} not found")
                except ValueError:
                    await websocket.send_text("Error: Invalid todo_id")
                    logger.error("delete-todo command failed: Invalid todo_id")

            elif command == "help":
                help_text = """
Available Commands:
  list-todos           List all todos.
  get-todo <todo_id>   Get a todo by ID.
  create-todo <title> [description]  Create a new todo.
  update-todo <todo_id> <title> [description] [--completed]  Update a todo by ID.
  delete-todo <todo_id> Delete a todo by ID.
  exit                 Exit the WebSocket session.

Usage Examples:
  List all todos:
    list-todos

  Get a todo by ID:
    get-todo 1

  Create a new todo:
    create-todo "New Task" "Task description"

  Update a todo by ID:
    update-todo 1 "Updated Task" "Updated description" --completed

  Delete a todo by ID:
    delete-todo 1

  Exit the WebSocket session:
    exit
"""
                await websocket.send_text(help_text)
                logger.info("help command executed")

            elif command == "exit":
                await websocket.send_text("Exiting WebSocket session.")
                logger.info("exit command executed")
                break

            else:
                await websocket.send_text(f"Error: Command '{command}' not supported")
                logger.error(f"Unsupported command '{command}' received")
    except Exception as e:
        logger.error(f"WebSocket error: {e}")
        await websocket.close()
