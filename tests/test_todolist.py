"""Test suite for the Todo list application. 
  Note that normally you would have more than one test module 
  but here we use one for simplicity.
"""

import sys
from pathlib import Path

# Add the parent directory to the Python path
sys.path.append(str(Path(__file__).parent.parent))

from typing import List
from todolist import Todo


def test_add_task() -> None:
    """Test the add_task method of the Todo class.

    This test verifies that:
    - A valid task can be added to the list
    - The task appears in the tasks list after addition
    """
    todo = Todo()
    todo.add_task("Test task")
    assert "Test task" in todo.tasks


def test_delete_task() -> None:
    """Test the delete_task method of the Todo class.

    This test verifies that:
    - An existing task can be deleted from the list
    - The task is removed from the tasks list after deletion
    """
    todo = Todo()
    todo.add_task("Test task")
    todo.delete_task("Test task")
    assert "Test task" not in todo.tasks


def test_show_tasks_empty() -> None:
    """Test the show_tasks method with an empty task list.

    This test verifies that:
    - The tasks list can be empty
    - The show_tasks method handles empty lists correctly
    """
    todo = Todo()
    assert len(todo.tasks) == 0


def test_show_tasks_populated() -> None:
    """Test the show_tasks method with a populated task list.

    This test verifies that:
    - Multiple tasks can be added to the list
    - All added tasks are present in the list
    """
    todo = Todo()
    test_tasks: List[str] = ["Task 1", "Task 2", "Task 3"]
    for task in test_tasks:
        todo.add_task(task)
    assert len(todo.tasks) == len(test_tasks)
    for task in test_tasks:
        assert task in todo.tasks
