# todo-swagger-api

## Overview

This project consists of two main components:
- **API**: Manages the backend operations and data handling.
- **CLI**: Provides a command line interface to interact with the API.

## Installation

1. Clone the repository:

```bash
git clone [todo-swagger-api.git](https://github.com/mydadisalive/todo-swagger-api.git)
cd todo-swagger-api
```

2. Set up a virtual environment (recommended):

```bash
python -m venv venv
source venv/bin/activate # On Windows: .\venv\Scripts\activate
```

3. Install dependencies for both the API and CLI:

```bash
pip install -r requirements.txt
```

## Running the Project

### Running the API
To run the API server using Uvicorn:

```bash
uvicorn api.main:app --reload
```

The API will be available at: [http://127.0.0.1:8000](http://127.0.0.1:8000)

### Using the CLI
To use the CLI:

```bash
python cli/cli.py --help
```

List all todos
```bash
python cli/cli.py list-todos
```

Create a new todo:
```bash
python cli/cli.py create-todo "New Todo Title" "Optional description"
```

Get a todo by ID:
```bash
python cli/cli.py get-todo <todo_id>
```

Update a todo by ID:
```bash
python cli/cli.py update-todo <todo_id> "Updated Title" "Updated description"
```

Delete a todo by ID:
```bash
python cli/cli.py delete-todo <todo_id>
```

## WebSocket Functionality
In addition to the traditional REST API and CLI, this project also supports WebSocket for real-time communication.

To use the WebSocket functionality, run the following command:

```bash
python cli/cli.py websocket
```

Once connected, you can enter commands interactively. Supported commands include:

List all todos
list-todos

Expected Response:
[{"id": 1, "title": "Buy groceries", "description": "Milk, Bread, Cheese", "completed": False}, {"id": 2, "title": "Read a book", "description": "The Catcher in the Rye", "completed": False}]

Get a todo by ID
get-todo 1

Expected Response:
{"id": 1, "title": "Buy groceries", "description": "Milk, Bread, Cheese", "completed": False}

Create a new todo
create-todo "New Task" "Description of the new task"

Expected Response:
Created todo: {"id": 3, "title": "New Task", "description": "Description of the new task", "completed": False}

## API Documentation
Explore the API endpoints using Swagger UI:

Swagger UI: [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs)
ReDoc: [http://127.0.0.1:8000/redoc](http://127.0.0.1:8000/redoc)

## Testing

Run tests for both the API and CLI:

```bash
bash run_tests.sh # or pytest
```

Instructions on how to run specific tests and any additional setup required for testing environments.

## Contributing

Guidelines on how to contribute to the project. Include instructions for both API and CLI components, if different.

## License

Specify the license under which the project is released.
