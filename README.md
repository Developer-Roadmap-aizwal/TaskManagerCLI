# Task Manager CLI
Task Tracker CLI project from roadmap.sh https://roadmap.sh/projects/task-tracker <br>

A simple command-line task manager written in Python.

## Features

- Add tasks with descriptions.
- Update existing task descriptions.
- Delete tasks by ID.
- Mark tasks as "todo", "in-progress", or "done".
- List all tasks or filter by status.
- Tasks are saved in a JSON file for persistence.

## Usage

1. **Add a task:**

   ```bash
   python task_cli.py add "Finish project report"
2. **Update a task:**
   ```bash
   python task_cli.py update <task_id> "Updated task description"

3. **Delete a task:**
   ```bash
   python task_cli.py delete <task_id>

4. **Mark a task as done:**
   ```bash
    python task_cli.py mark <task_id> done

5. **List all tasks:**
   ```bash
   python task_cli.py list
6. **List tasks with a specific status:**
   ```bash
    python task_cli.py list in-progress

**Task Statuses**<br>
todo: The task is yet to be started. <br>
in-progress: The task is currently being worked on. <br>
done: The task has been completed. <br>

**Data Storage**<br>
Tasks are stored in a JSON file named tasks.json in the same directory as the script.<br>

Example
```bash
# Add some tasks
python task_cli.py add "Write unit tests"
python task_cli.py add "Deploy to staging"

# List all tasks
python task_cli.py list

# Mark a task as in-progress
python task_cli.py mark <task_id> in-progress

# Update a task description
python task_cli.py update <task_id> "Deploy to production"

# Delete a task
python task_cli.py delete <task_id>

# List completed tasks
python task_cli.py list done
```

Additional Notes:
The script uses uuid to generate unique IDs for tasks.
Timestamps for task creation and updates are recorded in ISO format.
