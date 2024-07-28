import subprocess
import pytest
from faker import Faker
from unittest.mock import patch, MagicMock

fake = Faker()

def run_cli_command(command):
    result = subprocess.run(command, shell=True, capture_output=True, text=True)
    return result

def reset_todos():
    # Explicitly clear and reset todos
    run_cli_command('python cli/auto_generated_cli.py delete-todo-by-id 1')
    run_cli_command('python cli/auto_generated_cli.py delete-todo-by-id 2')
    run_cli_command('python cli/auto_generated_cli.py delete-todo-by-id 3')
    run_cli_command('python cli/auto_generated_cli.py delete-todo-by-id 4')
    run_cli_command('python cli/auto_generated_cli.py delete-todo-by-id 5')
    run_cli_command('python cli/auto_generated_cli.py delete-todo-by-id 6')
    run_cli_command('python cli/auto_generated_cli.py delete-todo-by-id 7')
    run_cli_command('python cli/auto_generated_cli.py delete-todo-by-id 8')
    run_cli_command('python cli/auto_generated_cli.py delete-todo-by-id 9')
    run_cli_command('python cli/auto_generated_cli.py delete-todo-by-id 10')
    run_cli_command('python cli/auto_generated_cli.py create-todo-cmd "Buy groceries" "Milk, Bread, Cheese"')
    run_cli_command('python cli/auto_generated_cli.py create-todo-cmd "Read a book" "The Catcher in the Rye"')

@pytest.fixture(scope="function", autouse=True)
def setup_and_teardown():
    # Setup: Reset todos
    reset_todos()
    yield
    # Teardown: Clean up after tests
    reset_todos()

def test_list_todos():
    result = run_cli_command("python cli/auto_generated_cli.py list-todos")
    assert result.returncode == 0
    output = result.stdout.strip()
    assert "ID: 1, Title: Buy groceries, Completed: False" in output
    assert "ID: 2, Title: Read a book, Completed: False" in output

def test_create_todo():
    result = run_cli_command('python cli/auto_generated_cli.py create-todo-cmd "Test Todo" "This is a test todo"')
    assert result.returncode == 0
    output = result.stdout.strip()
    assert "Created todo: ID: 3, Title: Test Todo, Completed: False" in output

def test_get_todo():
    result = run_cli_command("python cli/auto_generated_cli.py get-todo-by-id 1")
    assert result.returncode == 0
    output = result.stdout.strip()
    assert "ID: 1, Title: Buy groceries, Completed: False" in output

def test_update_todo():
    result = run_cli_command('python cli/auto_generated_cli.py update-todo-by-id 1 "Updated Todo" "Updated description"')
    assert result.returncode == 0
    output = result.stdout.strip()
    assert "Updated todo: ID: 1, Title: Updated Todo, Completed: False" in output

def test_delete_todo():
    result = run_cli_command("python cli/auto_generated_cli.py delete-todo-by-id 1")
    assert result.returncode == 0
    output = result.stdout.strip()
    assert "Deleted todo: ID: 1" in output  # Check for ID only since title may vary

# New test using Faker
def test_create_todo_with_faker():
    title = fake.catch_phrase()  # Generates a realistic task title
    description = fake.text(max_nb_chars=50)  # Generates a short description
    result = run_cli_command(f'python cli/auto_generated_cli.py create-todo-cmd "{title}" "{description}"')
    assert result.returncode == 0
    output = result.stdout.strip()
    assert f"Created todo: ID: 3, Title: {title}, Completed: False" in output

# New test using mock
def test_list_todos_with_mock():
    mock_output = "ID: 1, Title: Buy groceries, Completed: False\nID: 2, Title: Read a book, Completed: False\n"
    mock_result = MagicMock()
    mock_result.returncode = 0
    mock_result.stdout = mock_output

    with patch('subprocess.run', return_value=mock_result) as mock_run:
        result = run_cli_command("python cli/auto_generated_cli.py list-todos")
        assert result.returncode == 0
        output = result.stdout.strip()
        assert "ID: 1, Title: Buy groceries, Completed: False" in output
        assert "ID: 2, Title: Read a book, Completed: False" in output
        mock_run.assert_called_once_with("python cli/auto_generated_cli.py list-todos", shell=True, capture_output=True, text=True)
