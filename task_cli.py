import sys
import json
import os
from datetime import datetime
import uuid

TASKS_FILE = "tasks.json"

def load_tasks():
    if not os.path.exists(TASKS_FILE):
        return []
    with open(TASKS_FILE, 'r') as f:
        return json.load(f)

def save_tasks(tasks):
    with open(TASKS_FILE, 'w') as f:
        json.dump(tasks, f, indent=2, default=str)

def add_task(description):
    tasks = load_tasks()
    new_task = {
        "id": str(uuid.uuid4()),
        "description": description,
        "status": "todo",
        "createdAt": datetime.now().isoformat(),
        "updatedAt": datetime.now().isoformat()
    }
    tasks.append(new_task)
    save_tasks(tasks)
    print(f"Task '{description}' added successfully with ID: {new_task['id']}")

def update_task(task_id, description):
    tasks = load_tasks()
    for task in tasks:
        if task['id'] == task_id:
            task['description'] = description
            task['updatedAt'] = datetime.now().isoformat()
            save_tasks(tasks)
            print(f"Task with ID {task_id} updated successfully.")
            return
    print(f"No task found with ID {task_id}")

def delete_task(task_id):
    tasks = load_tasks()
    initial_length = len(tasks)
    tasks = [task for task in tasks if task['id'] != task_id]
    if len(tasks) < initial_length:
        save_tasks(tasks)
        print(f"Task with ID {task_id} deleted successfully.")
    else:
        print(f"No task found with ID {task_id}")

def mark_task(task_id, status):
    if status not in ['todo', 'in-progress', 'done']:
        print("Invalid status. Use 'todo', 'in-progress', or 'done'.")
        return
    tasks = load_tasks()
    for task in tasks:
        if task['id'] == task_id:
            task['status'] = status
            task['updatedAt'] = datetime.now().isoformat()
            save_tasks(tasks)
            print(f"Task with ID {task_id} marked as '{status}'.")
            return
    print(f"No task found with ID {task_id}")

def list_tasks(filter_status=None):
    tasks = load_tasks()
    if filter_status:
        filtered_tasks = [task for task in tasks if task["status"] == filter_status]
    else:
        filtered_tasks = tasks
    
    if not filtered_tasks:
        print("No tasks found.")
    else:
        for task in filtered_tasks:
            print(f"ID: {task['id']}")
            print(f"Description: {task['description']}")
            print(f"Status: {task['status']}")
            print(f"Created At: {task['createdAt']}")
            print(f"Updated At: {task['updatedAt']}")
            print("--------------------")

def main():
    if len(sys.argv) < 2:
        print("Usage: python task_cli.py <action> [arguments]")
        return

    action = sys.argv[1]

    if action == "add" and len(sys.argv) == 3:
        add_task(sys.argv[2])
    elif action == "update" and len(sys.argv) == 4:
        update_task(sys.argv[2], sys.argv[3])
    elif action == "delete" and len(sys.argv) == 3:
        delete_task(sys.argv[2])
    elif action == "mark" and len(sys.argv) == 4:
        mark_task(sys.argv[2], sys.argv[3])
    elif action == "list":
        if len(sys.argv) == 2:
            list_tasks()
        elif len(sys.argv) == 3:
            list_tasks(sys.argv[2])
        else:
            print("Invalid number of arguments for list action.")
    else:
        print("Invalid action or number of arguments.")

if __name__ == "__main__":
    main()