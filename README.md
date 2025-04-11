# To-Do List Application

A simple command-line To-Do List application implemented in Python.

## Installation

1. Clone this repository:
   ```bash
   git clone <repository-url>
   cd todo-app
   ```

2. Create a virtual environment (recommended):
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

## Current Implementation

The application currently provides the following core functionality:

- **Task Management**
  - Add new tasks to the list
  - Delete existing tasks
  - View all tasks with numbered list
  - Input validation for empty tasks
  - Task existence checking before deletion

- **User Interface**
  - Interactive command-line menu
  - Clear option prompts
  - Success/error messages for operations
  - Continuous operation until user quits

- **Data Structure**
  - In-memory task storage using Python list
  - Simple and efficient task operations
  - Basic task validation

## Testing

The application includes a test suite using pytest. To run the tests:

1. Make sure you've installed the dependencies from requirements.txt
2. Run the tests:
   ```bash
   pytest tests/
   ```

## Usage Instructions

1. Clone this repository. 
2. Run the application using the command: `python todolist.py`.
3. To run the tests, use the command: `pytest tests/`. For more verbose output, use: `pytest -vs tests/`.
4. Use the menu options to add, delete, or view tasks.
5. Enhance the application by implementing the features listed above.

## In-Class Exercise

For detailed instructions about the in-class exercise, please see [in_class_exercise.md](in_class_exercise.md).
