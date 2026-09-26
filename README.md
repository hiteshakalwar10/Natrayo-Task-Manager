# NATRAYO Task Manager

A simple command-line Task Management System built with Python.

## Features

The application allows users to:

- Create a task
- List all tasks
- Get a task by ID
- Update a task
- Delete a task
- Complete a task
- Search tasks by title or description
- Exit the application

## Technology

- Python
- Command-Line Interface (CLI)
- In-memory storage
- Git and GitHub for version control

## Version 1 Scope

Version 1 does not use:

- Web frameworks
- Databases
- AI frameworks

Tasks are stored only in memory while the application is running.

## Task Information

Each task contains:

- ID
- Title
- Description
- Status
- Created_at

## Status Values

The application uses:

- `pending`
- `in_progress`
- `completed`

New tasks start with the status `in_progress`.

## Validation

The application validates:

- Required task title
- Task IDs
- Status values
- Menu choices
- Other invalid user input

The application should handle invalid input without crashing.

## Project Structure

```text
Natrayo-Task-Manager/
├── src/
├── tests/
├── DESIGN.md
├── ARCHITECTURE.md
├── LEARNINGS.md
├── BUGS_AND_DEBUGGING.md
├── README.md
├── .gitignore
└── main.py
```

## Setup

Clone the repository and move into the project directory.

```bash
git clone <repository-url>
cd Natrayo-Task-Manager
```

No external database or web framework is required for Version 1.
Python 3 is required.

## Running the Application

Run:

```bash
python main.py
```

The application displays a menu:

```text
===== NATRAYO TASK MANAGER =====
1. Create Task
2. List All Tasks
3. Get Task
4. Update Task
5. Delete Task
6. Complete Task
7. Search Tasks
8. Exit
```

Select an option by entering its number.

## Example Usage

Example task creation:

```text
Enter your choice: 1
Enter task title: Learn Python
Enter task description: Practice Python programming

Task created successfully.

ID: 1
Title: Learn Python
Description: Practice Python programming
Status: in_progress
```

Example search:

```text
Enter your choice: 7
Enter search term: python
```

The application displays matching tasks.

## Design

The application separates the task data model from task-management operations.

`Task` represents an individual task.

`TaskManager` manages the collection of tasks and provides operations such as:

- Create
- List
- Get
- Update
- Delete
- Complete
- Search

The CLI in `main.py` handles user interaction and calls the task-management methods.

## Architecture

The application follows a simple layered structure:

```text
User
  |
  v
CLI (main.py)
  |
  v
TaskManager
  |
  v
Task
  |
  v
In-Memory List
```

This keeps user interaction separate from the core task-management logic.

## Testing

The application was tested using normal operations and edge cases.

Tested scenarios include:

- Creating tasks
- Listing tasks
- Getting tasks by ID
- Updating tasks
- Deleting tasks
- Completing tasks
- Searching tasks
- Empty task titles
- Invalid task IDs
- Search with no results
- Invalid menu choices
- Empty task list

Debugging records are documented in `BUGS_AND_DEBUGGING.md`.

## Git Workflow

Git was used to manage the project history.

The workflow included:

```text
Working Directory
      |
      v
Staging Area
      |
      v
Commit
      |
      v
Feature Branch
      |
      v
Remote Repository
```

A feature branch was used for task-management implementation before merging the completed work into `master`.

## Known Limitations

Version 1 has the following limitations:

- Tasks are stored only in memory.
- Tasks are lost when the application exits.
- There is no database.
- There is no web interface.
- There is no authentication.
- The application is designed for CLI use.

## Future Improvements

Possible future improvements include:

- Persistent database storage
- REST API
- Web interface
- Automated test suite
- Better search and filtering
- User authentication
- Task priorities and due dates