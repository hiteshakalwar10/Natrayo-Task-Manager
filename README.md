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