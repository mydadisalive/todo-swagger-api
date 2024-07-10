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
uvicorn api.main --reload
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
