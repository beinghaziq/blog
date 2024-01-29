# console.py

import os
from main import app
from fastapi.testclient import TestClient
import importlib
from prompt_toolkit import prompt
from prompt_toolkit.key_binding import KeyBindings
from prompt_toolkit.keys import Keys

client = TestClient(app)
kb = KeyBindings()
history = []
history_index = 0


def import_repositories():
    repository_path = os.path.join(
        os.path.dirname(__file__), "app", "repositories")
    repositories = {}

    for filename in os.listdir(repository_path):
        if filename.endswith(".py") and not filename.startswith("__"):
            module_name = os.path.splitext(filename)[0]
            module = importlib.import_module(f"app.repositories.{module_name}")
            for name in dir(module):
                if name.endswith("Repository") and callable(getattr(module, name)) and name != "BaseRepository":
                    repositories[name] = getattr(module, name)()

    return repositories


def execute_command(command: str, repositories):
    try:
        # Include repositories in the global context
        globals().update(repositories)

        # Execute the command
        result = eval(command, globals())
        return result
    except Exception as e:
        return f"Error executing command: {str(e)}"


@kb.add(Keys.ControlC)
def _(event):
    """
    Pressing Ctrl+C will exit the application. This is optional.
    """
    event.app.exit()


@kb.add('up')
def arrow_up(event):
    global history_index
    if history:
        history_index = max(0, history_index - 1)
        event.app.current_buffer.text = history[history_index]


@kb.add('down')
def arrow_down(event):
    global history_index
    if history:
        history_index = min(len(history) - 1, history_index + 1)
        event.app.current_buffer.text = history[history_index]


@kb.add('right')
def arrow_right(event):
    event.app.current_buffer.cursor_position += 1


@kb.add('left')
def arrow_left(event):
    event.app.current_buffer.cursor_position -= 1

if __name__ == "__main__":
    # Import all repositories and create instances
    repositories = import_repositories()

    while True:
        command = prompt("> ", key_bindings=kb,
                         mouse_support=True)
        if command.lower() == "exit":
            break

        if command:
            history.append(command)
            history_index = len(history)

        result = execute_command(command, repositories)

        if hasattr(result, "__repr__") and callable(result.__repr__):
            # Check if the result has a __repr__ method and call it
            repr_result = repr(result)
            print("Result:", repr_result)
        else:
            print("Result:", result)

