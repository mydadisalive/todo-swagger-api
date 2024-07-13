from fast_api_client.client import Client
from fast_api_client.models.todo import Todo
from fast_api_client.models.todo_create import TodoCreate
from fast_api_client.api.default.get_todo_todos_todo_id_get import sync_detailed as get_todo_by_id
from fast_api_client.api.default.create_todo_todos_post import sync_detailed as create_todo

# Create a client instance
client = Client(base_url="http://127.0.0.1:8000")

# Example: Get a todo item
todo_id = 1
response = get_todo_by_id(client=client, todo_id=todo_id)
if response.status_code == 200:
    todo = response.parsed
    print(f"Todo ID: {todo.id}, Title: {todo.title}, Description: {todo.description}, Completed: {todo.completed}")
else:
    print(f"Failed to get todo: {response.status_code}")

# Example: Create a new todo item
new_todo = TodoCreate(
    title="New Task",
    description="New Task Description",
    completed=False
)
response = create_todo(client=client, body=new_todo)
if response.status_code == 201:
    created_todo = response.parsed
    print(f"Created Todo: {created_todo}")
else:
    print(f"Failed to create todo: {response.status_code}
