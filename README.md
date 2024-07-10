# todo-swagger-api

## Overview

This project consists of two main components:
- **API**: Manages the backend operations and data handling.
- **CLI**: Provides a command line interface to interact with the API.

## Installation

1. Clone the repository:

git clone [<repository-url>](https://github.com/mydadisalive/todo-swagger-api.git)
cd todo-swagger-api


2. Set up a virtual environment (recommended):
python -m venv venv
source venv/bin/activate # On Windows: .\venv\Scripts\activate

3. Install dependencies for both the API and CLI:
pip install -r requirements.txt


## Running the Project

### Running the API
To run the API server using Uvicorn:
uvicorn api.main --reload

The API will be available at: [http://127.0.0.1:8000](http://127.0.0.1:8000)

### Using the CLI
To use the CLI:
python cli/cli.py --help

Explore how to use different CLI commands that interact with the API.

## API Documentation

Explore the API endpoints using Swagger UI:
[Swagger UI: http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs)

## Testing

Run tests for both the API and CLI:
pytest

Instructions on how to run specific tests and any additional setup required for testing environments.

## Contributing

Guidelines on how to contribute to the project. Include instructions for both API and CLI components, if different.

## License

Specify the license under which the project is released.
