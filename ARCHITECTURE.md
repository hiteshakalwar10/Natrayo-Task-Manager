# NATRAYO Task Manager — Architecture

## 1. Overview

The NATRAYO Task Manager is a Python-based CLI application.

It allows the user to manage tasks through a command-line menu.

Version 1 uses in-memory storage, so tasks exist only while the application is running.

## 2. Architecture

                +----------------+
                |      User      |
                +-------+--------+
                        |
                        v
                +----------------+
                |  CLI / Input   |
                +-------+--------+
                        |
                        v
                +----------------------+
                |  Task Management     |
                |      Logic           |
                +----------+-----------+
                           |
              +------------+------------+
              |                         |
              v                         v
       +-------------+           +-------------+
       | Validation  |           | Task List  |
       +-------------+           |  (Memory)   |
                                 +-------------+
              |                         |
              +------------+------------+
                           |
                           v
                  +----------------+
                  |     Output     |
                  +----------------+
                           |
                           v
                         User

## 3.Components
# User

The user interacts with the application through the CLI.

# CLI / Input

Responsible for:

Displaying the main menu.
Reading user choices.
Reading task information.
Passing input to the task management logic.

# Task Management Logic

Responsible for:

Creating tasks.
Listing tasks.
Getting a task by ID.
Updating tasks.
Deleting tasks.
Completing tasks.
Searching tasks.

# Validation

Responsible for checking:

Required title.
Valid task IDs.
Valid status values.
Valid menu choices.
Other invalid user input.

# Task List

Stores all tasks in memory using a Python list.

# Output

Displays:

Task information.
Success messages.
Error messages.
Search results.
Validation messages.

## 4. Main Control Flow
Start Application
       |
       v
Display Menu
       |
       v
Get User Choice
       |
       +---- Create ------> Validate ---> Store Task
       |
       +---- List --------> Get Tasks --> Display
       |
       +---- Get ---------> Find ID ----> Display
       |
       +---- Update ------> Find ID ----> Update
       |
       +---- Delete ------> Find ID ----> Confirm ---> Delete
       |
       +---- Complete ----> Find ID ----> Set completed
       |
       +---- Search ------> Search Title/Description
       |
       +---- Exit --------> End Program
       |
       v
Return to Menu

## 5. Data Flow

For a new task:

User Input
    ↓
Validate Input
    ↓
Generate Task ID
    ↓
Set Status
    ↓
Set Created Time
    ↓
Create Task
    ↓
Add to Task List
    ↓
Display Success Message

## 6. Storage

Version 1 uses an in-memory Python list.

Example:

tasks = [
    Task 1,
    Task 2,
    Task 3
]

No database or persistent storage is used in Version 1.

## 7. Error Handling Flow
User Input
    ↓
Validation
    |
    +---- Valid ------> Perform Operation
    |
    +---- Invalid ----> Show Error
                              |
                              v
                         Ask Again

The application should handle invalid input without crashing.


Then press **Ctrl + S**                      