import click
import requests
from typing import List

# Define the base URL for your FastAPI server
base_url = "http://127.0.0.1:8000"

@click.group()
def cli():
    pass

@cli.command()
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

@cli.command()
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

@cli.command()
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

@cli.command()
@click.argument('todo_id', type=int)
@click.argument('title')
@click.argument('description', required=False)
def update_todo(todo_id, title, description=None):
    """Update a todo by ID."""
    try:
        payload = {"id": todo_id, "title": title, "description": description, "completed": False}
        response = requests.put(f"{base_url}/todos/{todo_id}", json=payload)
        response.raise_for_status()  # Raise exception for bad response (4xx or 5xx)
        todo = response.json()
        click.echo(f"Updated todo: ID: {todo['id']}, Title: {todo['title']}, Completed: {todo['completed']}")
    except requests.exceptions.RequestException as e:
        click.echo(f"Error: {e}")

@cli.command()
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

if __name__ == '__main__':
    cli()
