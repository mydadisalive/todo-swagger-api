import click
import requests
import asyncio
import websockets
from typing import Optional

# Define the base URL for your FastAPI server
base_url = "http://127.0.0.1:8000"
websocket_url = "ws://127.0.0.1:8000/ws"  # Adjust as needed

@click.group()
def cli():
    """A simple CLI to interact with the Todo API."""
    pass

@cli.command(name="list-todos")
def list_todos():
    """List all todos."""
    try:
        response = requests.get(f"{base_url}/todos")
        response.raise_for_status()  # Raise exception for bad response (4xx or 5xx)
        todos = response.json()
        for todo in todos:
            click.echo(f"ID: {todo['id']}, Title: {todo['title']}, Completed: {todo['completed']}")
    except requests.exceptions.RequestException as e:
        click.echo(f"Error: {e}")

@cli.command(name="get-todo")
@click.argument('todo_id', type=int)
def get_todo(todo_id):
    """Get a todo by ID."""
    try:
        response = requests.get(f"{base_url}/todos/{todo_id}")
        response.raise_for_status()  # Raise exception for bad response (4xx or 5xx)
        todo = response.json()
        click.echo(f"ID: {todo['id']}, Title: {todo['title']}, Completed: {todo['completed']}")
    except requests.exceptions.RequestException as e:
        click.echo(f"Error: {e}")

@cli.command(name="create-todo")
@click.argument('title')
@click.argument('description', required=False)
def create_todo(title, description=None):
    """Create a new todo."""
    try:
        payload = {"title": title, "description": description, "completed": False}
        response = requests.post(f"{base_url}/todos", json=payload)
        response.raise_for_status()  # Raise exception for bad response (4xx or 5xx)
        todo = response.json()
        click.echo(f"Created todo: ID: {todo['id']}, Title: {todo['title']}, Completed: {todo['completed']}")
    except requests.exceptions.RequestException as e:
        click.echo(f"Error: {e}")

@cli.command(name="update-todo")
@click.argument('todo_id', type=int)
@click.argument('title')
@click.argument('description', required=False)
@click.option('--completed', is_flag=True, default=False, help="Mark the todo as completed.")
def update_todo(todo_id, title, description=None, completed=False):
    """Update a todo by ID."""
    try:
        payload = {"id": todo_id, "title": title, "description": description, "completed": completed}
        response = requests.put(f"{base_url}/todos/{todo_id}", json=payload)
        response.raise_for_status()  # Raise exception for bad response (4xx or 5xx)
        todo = response.json()
        click.echo(f"Updated todo: ID: {todo['id']}, Title: {todo['title']}, Completed: {todo['completed']}")
    except requests.exceptions.RequestException as e:
        click.echo(f"Error: {e}")

@cli.command(name="delete-todo")
@click.argument('todo_id', type=int)
def delete_todo(todo_id):
    """Delete a todo by ID."""
    try:
        response = requests.delete(f"{base_url}/todos/{todo_id}")
        response.raise_for_status()  # Raise exception for bad response (4xx or 5xx)
        todo = response.json()
        click.echo(f"Deleted todo: ID: {todo['id']}, Title: {todo['title']}, Completed: {todo['completed']}")
    except requests.exceptions.RequestException as e:
        click.echo(f"Error: {e}")

@cli.command(name="websocket")
def websocket_command():
    """Connect to the WebSocket server."""
    async def connect_websocket():
        async with websockets.connect(websocket_url) as websocket:
            click.echo("Connected to the WebSocket server.")
            try:
                while True:
                    command = input("Enter command: (type help for help) ")
                    await websocket.send(command)
                    response = await websocket.recv()
                    click.echo(f"Received: {response}")
                    if command == "exit":
                        break
            except websockets.exceptions.ConnectionClosed:
                click.echo("WebSocket connection closed")
            finally:
                await websocket.close()

    try:
        asyncio.run(connect_websocket())
    except Exception as e:
        click.echo(f"Error: {e}")

@cli.command(name="help")
def help_command():
    """Prints the available commands and usage examples."""
    help_text = """
Available Commands:
  list-todos           List all todos.
  get-todo <todo_id>   Get a todo by ID.
  create-todo <title> [description]  Create a new todo.
  update-todo <todo_id> <title> [description] [--completed]  Update a todo by ID.
  delete-todo <todo_id> Delete a todo by ID.
  websocket            Connect to the WebSocket server.

Usage Examples:
  List all todos:
    python cli/cli.py list-todos

  Get a todo by ID:
    python cli/cli.py get-todo 1

  Create a new todo:
    python cli/cli.py create-todo "New Task" "Task description"

  Update a todo by ID:
    python cli/cli.py update-todo 1 "Updated Task" "Updated description" --completed

  Delete a todo by ID:
    python cli/cli.py delete-todo 1

  Connect to the WebSocket server:
    python cli/cli.py websocket
"""
    click.echo(help_text)

if __name__ == '__main__':
    cli()
