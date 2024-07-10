import subprocess
import pytest
import time

# Fixture to start and stop the server
@pytest.fixture(scope="module", autouse=True)
def start_server():
    # Start the server
    server = subprocess.Popen(["uvicorn", "api.main:app", "--reload"])
    time.sleep(2)  # Wait for the server to start
    yield
    # Stop the server
    server.terminate()
    server.wait()

def run_cli_command(command):
    result = subprocess.run(command, shell=True, capture_output=True, text=True)
    return result

def test_list_todos():
    result = run_cli_command("python cli/cli.py list-todos")
    assert result.returncode == 0
    output = result.stdout.strip()
    assert "ID: 1, Title: Buy groceries, Completed: False" in output
    assert "ID: 2, Title: Read a book, Completed: False" in output

def test_create_todo():
    result = run_cli_command('python cli/cli.py create-todo "Test Todo" "This is a test todo"')
    assert result.returncode == 0
    output = result.stdout.strip()
    assert "Created todo: ID:" in output

def test_get_todo():
    result = run_cli_command("python cli/cli.py get-todo 1")
    assert result.returncode == 0
    output = result.stdout.strip()
    assert "ID: 1, Title: Buy groceries, Completed: False" in output

def test_update_todo():
    result = run_cli_command('python cli/cli.py update-todo 1 "Updated Todo" "Updated description"')
    assert result.returncode == 0
    output = result.stdout.strip()
    assert "Updated todo: ID: 1, Title: Updated Todo, Completed: False" in output

def test_delete_todo():
    result = run_cli_command("python cli/cli.py delete-todo 1")
    assert result.returncode == 0
    output = result.stdout.strip()
    assert "Deleted todo: ID: 1" in output  # Check for ID only since title may vary
