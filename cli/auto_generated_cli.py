import click
from fast_api_client import Client
from fast_api_client.api.default import (
    get_todos_todos_get,
    create_todo_todos_post,
    get_todo_todos_todo_id_get,
    update_todo_todos_todo_id_put,
    delete_todo_todos_todo_id_delete,
)
from fast_api_client.models.todo_create import TodoCreate  # Adjust the import based on actual structure
from fast_api_client.models.todo import Todo
from fast_api_client.errors import UnexpectedStatus

client = Client(base_url="http://127.0.0.1:8000")

@click.group()
def cli():
    pass

@cli.command()
def list_todos():
    """List all todos."""
    try:
        todos = get_todos_todos_get.sync(client=client)
        for todo in todos:
            click.echo(f"ID: {todo.id}, Title: {todo.title}, Completed: {todo.completed}")
    except UnexpectedStatus as e:
        click.echo(f"Error: {e}")

@cli.command()
@click.argument("title")
@click.argument("description", required=False)
def create_todo_cmd(title, description):
    """Create a new todo."""
    todo_create = TodoCreate(title=title, description=description)
    try:
        new_todo = create_todo_todos_post.sync(client=client, body=todo_create)
        click.echo(f"Created todo: ID: {new_todo.id}, Title: {new_todo.title}, Completed: {new_todo.completed}")
    except UnexpectedStatus as e:
        click.echo(f"Error: {e}")

@cli.command()
@click.argument("todo_id", type=int)
def get_todo_by_id(todo_id):
    """Get a todo by ID."""
    try:
        todo = get_todo_todos_todo_id_get.sync(client=client, todo_id=todo_id)
        click.echo(f"ID: {todo.id}, Title: {todo.title}, Completed: {todo.completed}")
    except UnexpectedStatus as e:
        click.echo(f"Error: {e}")

@cli.command()
@click.argument("todo_id", type=int)
@click.argument("title")
@click.argument("description", required=False)
@click.option("--completed", is_flag=True, help="Mark the todo as completed")
def update_todo_by_id(todo_id, title, description, completed):
    """Update a todo by ID."""
    todo_update = Todo(title=title, description=description, completed=completed, id=todo_id)  # Using Todo model
    try:
        updated_todo = update_todo_todos_todo_id_put.sync(client=client, todo_id=todo_id, body=todo_update)
        click.echo(f"Updated todo: ID: {updated_todo.id}, Title: {updated_todo.title}, Completed: {updated_todo.completed}")
    except UnexpectedStatus as e:
        click.echo(f"Error: {e}")

@cli.command()
@click.argument("todo_id", type=int)
def delete_todo_by_id(todo_id):
    """Delete a todo by ID."""
    try:
        deleted_todo = delete_todo_todos_todo_id_delete.sync(client=client, todo_id=todo_id)
        click.echo(f"Deleted todo: ID: {deleted_todo.id}, Title: {deleted_todo.title}, Completed: {deleted_todo.completed}")
    except UnexpectedStatus as e:
        click.echo(f"Error: {e}")

if __name__ == "__main__":
    cli()
