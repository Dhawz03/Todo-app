# To-Do List

This is a simple yet powerful To-Do List application built using Python and the Tkinter library. The app allows you to manage tasks by adding, editing, deleting, saving, and loading tasks. The interface is intuitive, with options to set task priorities and deadlines.

## Features

- **Add Tasks:** Add tasks with a priority and a deadline.
- **Edit Tasks:** Edit existing tasks in the list.
- **Delete Tasks:** Remove tasks from the list.
- **Save Tasks:** Save your current list of tasks to a file.
- **Load Tasks:** Load a previously saved list of tasks.

## Prerequisites

Ensure you have Python 3 installed. This project also uses the `tkinter` and `tkcalendar` libraries, and it is set up in a virtual environment.

## Installation

1. Clone the repository:
    ```bash
    git clone https://github.com/Dhawz03/Todo-list.git
    cd todo-list-app
    ```

2. Set up a virtual environment:
    ```bash
    python -m venv venv
    ```

3. Activate the virtual environment:

    - On Windows:
      ```bash
      .\venv\Scripts\activate
      ```
    - On macOS/Linux:
      ```bash
      source venv/bin/activate
      ```

4. Install the required packages:
    ```bash
    pip install -r requirements.txt
    ```

5. Run the application:
    ```bash
    python main.py
    ```

## File Structure

- `todo.py`: Contains the main `ToDoListApp` class that handles the GUI and functionality.
- `main.py`: The entry point of the application.
- `test_todo_list.py`: Contains unit tests for the application.

## Running Tests

To run the tests, make sure you're in the virtual environment and then run:
```bash
python -m unittest test_todo_list.py
