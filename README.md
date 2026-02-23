# Day 01 - CLI Task Manager

## Project Description

This is a simple command-line interface (CLI) task manager that allows users to add, list, complete, and delete tasks. Tasks can have a description, priority (high, medium, low), and an optional due date. All tasks are persisted to a `tasks.json` file.

## Features

*   **Add Task**: Add a new task with a description, priority, and optional due date.
*   **List Tasks**: View all tasks, sorted by completion status, priority, and due date.
*   **Complete Task**: Mark a task as completed.
*   **Delete Task**: Remove a task from the list.
*   **File Persistence**: Tasks are saved to and loaded from a `tasks.json` file, ensuring data is not lost between sessions.

## How to Run

1.  **Navigate to the project directory**:

    ```bash
    cd "Day 01 - CLI Task Manager"
    ```

2.  **Run the task manager**:

    ```bash
    python3 task_manager.py
    ```

## Usage

Upon running the script, you will be presented with a menu:

```
CLI Task Manager
1. Add Task
2. List Tasks
3. Complete Task
4. Delete Task
5. Exit
```

Follow the prompts to interact with the task manager.

### Example Workflow

1.  **Add a task**:
    ```
    Enter your choice: 1
    Enter task description: Buy groceries
    Enter priority (high, medium, low, default medium): high
    Enter due date (YYYY-MM-DD, optional): 2026-02-24
    Task 'Buy groceries' added.
    ```

2.  **List tasks**:
    ```
    Enter your choice: 2

    --- Your Tasks ---
    [ ] 1. Buy groceries (Priority: high) (Due: 2026-02-24)
    ------------------
    ```

3.  **Complete a task**:
    ```
    Enter your choice: 3
    Enter task ID to complete: 1
    Task 1 marked as completed.
    ```

4.  **List tasks again**:
    ```
    Enter your choice: 2

    --- Your Tasks ---
    [x] 1. Buy groceries (Priority: high) (Due: 2026-02-24)
    ------------------
    ```
