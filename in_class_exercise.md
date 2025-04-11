# CS322 W2 In-Class Exercise

Each student should create a new repository and use this repository as a template, let's refer to that repo as "MyRepo". Next, each student should fork *another student's* repository and implement a feature. We'll refer to that repo as "OtherRepo". DO NOT clone your own repository.

Here are the concrete steps to follow:

1. On github.com, fork "OtherRepo" belonging to another student (not your own "MyRepo"), let's call this "OtherRepoFork"
2. Clone your "OtherRepoFork" on your machine (preferably using ssh)
3. Create a new branch for your feature, e.g., `git switch -c feature/mark-completed`
4. Implement the feature of your choice. This involves:
   * Writing code to implement the feature
   * Adding tests for the new feature
   * Running the tests to ensure the feature works as expected
   * Updating the README file to reflect the new feature
5. Commit and push changes to "OtherRepoFork" (you do this repeatedly as you work on the feature)
6. Create a pull request from "OtherRepoFork" to "MyRepo" (you can do this at any time after creating the branch)
7. When you are ready, request a code review from another student in your Pull Request (PR) in "OtherRepo"
8. Make changes (commit and push) in response to comments as needed. Respond to each comment. Iterate until the PR is approved.
8. After the PR is approved by "OtherRepo"'s owner, you can merge your changes into "OtherRepo"

## Features to Implement

- [ ] Edit task functionality
- [ ] Mark tasks as completed
- [ ] Save tasks to a file
- [ ] Load tasks from a file
- [ ] Task filtering (e.g., show completed, active tasks)
- [ ] Add task priority levels (High, Medium, Low)
- [ ] Sort tasks by priority
- [ ] Add due dates to tasks
- [ ] Show tasks due today
- [ ] Clear all tasks option
- [ ] Add task categories/tags
- [ ] Search tasks by keyword
- [ ] Count total number of tasks
- [ ] Add task descriptions
- [ ] Show task creation date

### What to Test

When implementing new features, consider testing:

- **Task Operations**
  - Adding valid and invalid tasks
  - Deleting existing and non-existent tasks
  - Viewing empty and populated task lists
  - Edge cases (empty strings, special characters)

- **New Features**
  - All new functionality should have corresponding tests
  - Test both success and failure cases
  - Include edge cases and boundary conditions
  - Test interactions between features

- **Data Persistence** (when implemented)
  - Saving and loading tasks
  - File handling errors
  - Data integrity

Example test structure:
```python
def test_add_task():
    todo = Todo()
    todo.add_task("Test task")
    assert "Test task" in todo.tasks

def test_delete_task():
    todo = Todo()
    todo.add_task("Test task")
    todo.delete_task("Test task")
    assert "Test task" not in todo.tasks
```
