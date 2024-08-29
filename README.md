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
```

## Usage

1. **Add Task:**
   - Enter the task name.
   - Select the priority (High, Medium, Low).
   - Pick a deadline date.
   - Click "Add Task" to add it to your list.

2. **Edit Task:**
   - Select the task from the list.
   - Click "Edit Task" and modify the text in the dialog that appears.

3. **Delete Task:**
   - Select the task from the list.
   - Click "Delete Task" to remove it.

4. **Save Tasks:**
   - Click "Save Tasks" to save the current tasks to a `.txt` file.

5. **Load Tasks:**
   - Click "Load Tasks" to load tasks from a saved `.txt` file.

## Dependencies

- `tkinter`: Python's standard GUI toolkit.
- `tkcalendar`: A calendar/date picker for Tkinter.
