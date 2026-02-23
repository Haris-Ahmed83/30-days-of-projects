
import json
import os
from datetime import datetime

TASKS_FILE = 'tasks.json'

def load_tasks():
    if os.path.exists(TASKS_FILE):
        with open(TASKS_FILE, 'r') as f:
            return json.load(f)
    return []

def save_tasks(tasks):
    with open(TASKS_FILE, 'w') as f:
        json.dump(tasks, f, indent=4)

def add_task(description, priority='medium', due_date=None):
    tasks = load_tasks()
    task = {
        'id': len(tasks) + 1,
        'description': description,
        'priority': priority,
        'due_date': due_date,
        'completed': False
    }
    tasks.append(task)
    save_tasks(tasks)
    print(f"Task '{description}' added.")

def list_tasks(filter_completed=False):
    tasks = load_tasks()
    if filter_completed:
        tasks = [task for task in tasks if not task['completed']]

    if not tasks:
        print("No tasks found.")
        return

    print("\n--- Your Tasks ---")
    for task in sorted(tasks, key=lambda x: (x['completed'], x['priority'], x['due_date'] or 'zzzz')):
        status = "[x]" if task['completed'] else "[ ]"
        due = f" (Due: {task['due_date']})" if task['due_date'] else ""
        print(f"{status} {task['id']}. {task['description']} (Priority: {task['priority']}){due}")
    print("------------------\n")

def complete_task(task_id):
    tasks = load_tasks()
    for task in tasks:
        if task['id'] == task_id:
            task['completed'] = True
            save_tasks(tasks)
            print(f"Task {task_id} marked as completed.")
            return
    print(f"Task {task_id} not found.")

def delete_task(task_id):
    tasks = load_tasks()
    initial_len = len(tasks)
    tasks = [task for task in tasks if task['id'] != task_id]
    if len(tasks) < initial_len:
        save_tasks(tasks)
        print(f"Task {task_id} deleted.")
    else:
        print(f"Task {task_id} not found.")

def main():
    while True:
        print("\nCLI Task Manager")
        print("1. Add Task")
        print("2. List Tasks")
        print("3. Complete Task")
        print("4. Delete Task")
        print("5. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            description = input("Enter task description: ")
            priority = input("Enter priority (high, medium, low, default medium): ").lower() or 'medium'
            due_date = input("Enter due date (YYYY-MM-DD, optional): ")
            if due_date and not datetime.strptime(due_date, '%Y-%m-%d'):
                print("Invalid date format. Please use YYYY-MM-DD.")
                continue
            add_task(description, priority, due_date)
        elif choice == '2':
            list_tasks()
        elif choice == '3':
            try:
                task_id = int(input("Enter task ID to complete: "))
                complete_task(task_id)
            except ValueError:
                print("Invalid task ID. Please enter a number.")
        elif choice == '4':
            try:
                task_id = int(input("Enter task ID to delete: "))
                delete_task(task_id)
            except ValueError:
                print("Invalid task ID. Please enter a number.")
        elif choice == '5':
            print("Exiting Task Manager.")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
