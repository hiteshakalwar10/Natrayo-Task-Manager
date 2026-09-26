# NATRAYO Task Manager — Learnings

## 1. Engineering Task Understanding

Before writing code, the task requirements were identified and converted into a clear design.

The main requirements are:

- Create tasks
- List tasks
- Get a task by ID
- Update tasks
- Delete tasks
- Complete tasks
- Search tasks
- Exit the application

## 2. Requirements vs Design Decisions

A requirement describes **what the system must do**.

A design decision describes **how we choose to implement it**.

Example:

Requirement:
- Every task must have a unique ID.

Design decision:
- Generate sequential integer IDs starting from 1.

## 3. CLI

CLI means **Command-Line Interface**.

It allows the user to interact with the application by entering commands or choosing options through the terminal.

This project uses a CLI instead of a web interface.

## 4. In-Memory Storage

Version 1 stores tasks in memory using a Python list.

This means:

- Tasks can be created and managed while the program is running.
- No database is required.
- Tasks are lost when the program exits.

## 5. Validation

Validation checks whether user input is acceptable before performing an operation.

Examples:

- Empty title should be rejected.
- Invalid task ID should be handled.
- Invalid status should be rejected.
- Invalid menu choices should be handled.

## 6. Edge Cases

An edge case is an unusual situation that the program must handle correctly.

Examples:

- No tasks exist.
- A task ID does not exist.
- Search returns no results.
- User enters an empty title.
- User enters an invalid status.
- User cancels a delete operation.

## 7. Git and Version Control

Git is used to track changes in the project.

Important Git concepts include:

- Working directory
- Staging area
- Commit
- Branch
- Merge
- Remote repository

The project will use descriptive commit messages that clearly explain what changed.

## 8. Testing and Debugging

The application will be tested after implementation.

The process will include:

1. Run the application.
2. Test normal operations.
3. Test edge cases.
4. Identify bugs.
5. Debug the code.
6. Run the tests again.
7. Document important bugs and fixes.

## 9. Main Engineering Learning

The main learning from this project is that software development is not only about writing code.

The process includes:

- Understanding requirements
- Making design decisions
- Planning architecture
- Implementing features
- Testing
- Debugging
- Using version control
- Documenting the work