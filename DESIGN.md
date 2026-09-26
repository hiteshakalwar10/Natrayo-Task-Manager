#Natrayo task manager - Design
## 1.problem

The goal is to build a CLI Task Management System where users can manage their tasks. The user can create, list, get, update, delete, complete and search tasks.

## 2.Task Model

Each task contains:

- ID
- Title
- Description
- Status
- Created_at

## 3.Requirements

The system must allow the user to:

1. Create a task
2. List all tasks
3. Get a task using its ID
4. Update a task
5. Delete a task
6. Complete a task
7. Search tasks by title or description
8. Exit the application

Each task must have a unique ID, title, description, status and created_at value.

## 4.Design Decisions

### Programming Language
Python will be used to implement the application.

### Interface
The application will use a Command-Line Interface (CLI).

### Storage
Tasks will be stored in memory. No database will be used in Version 1.

### Data Structure
A list will be used to store tasks in memory.

### Task ID
Task IDs will be generated automatically as sequential integers starting from 1. IDs will not be reused after a task is deleted.

### Initial Status
A newly created task will have the status 'in_progress'.

### Status Values
The allowed status values will be:
- pending
- in_progress
- completed

### Search
Search will check both the task title and description.

### Title
A task must have a title. An empty title will be rejected.

### Description
The description is optional.

### Created Time
The `created_at` value will be generated automatically using the current date and time.

### Update
The user can update the title, description or status. The task ID cannot be changed.

### Delete
The program will ask the user for confirmation before deleting a task.

### Get Task
The complete task information will be displayed, including ID, title, description, status, and created_at.

## 5.Control Flow

The application will start by displaying a menu of available operations.

The user will select an operation from the menu.

The program will then perform the selected operation:

- Create Task → collect task details and create a new task.
- List Tasks → display all existing tasks.
- Get Task → ask for an ID and display the matching task.
- Update Task → ask for an ID, show the current task and allow the user to update its information.
- Delete Task → ask for an ID, request confirmation and delete the task if confirmed.
- Complete Task → ask for an ID and change the task status to `completed`.
- Search Tasks → ask for a search term and display tasks matching the title or description.
- Exit → terminate the application.

After completing an operation, the program will return to the main menu until the user chooses Exit.

## 6.Validation and Error Handling

The program will validate user input before performing an operation.

### Validation Rules

- Task title cannot be empty.
- Task ID must refer to an existing task when using Get, Update, Delete or Complete.
- Status must be one of:
  - `pending`
  - `in_progress`
  - `completed`
- Invalid menu choices will be rejected.
- Empty search results will be handled without crashing.

### Error Handling

If the user enters invalid information, the program will show a clear error message and ask for valid input again.

If a task ID does not exist, the program will display:

"Task not found."

The program should handle invalid input without crashing.

## 7.Edge Cases

The application should handle the following edge cases:

1. Creating a task with an empty title.
2. Trying to get a task using an ID that does not exist.
3. Trying to update a task using an ID that does not exist.
4. Trying to delete a task using an ID that does not exist.
5. Trying to complete a task using an ID that does not exist.
6. Listing tasks when no tasks have been created.
7. Searching when no tasks match the search term.
8. Entering an invalid menu option.
9. Entering an invalid status.
10. Trying to delete a task and choosing "No" during confirmation.
11. Trying to complete a task that is already completed.

## 8.Data Flow

The general data flow of the application is:

User
  ↓
CLI / Input
  ↓
Task Management Logic
  ↓
In-Memory Task List
  ↓
Output
  ↓
User

For creating a task:

User enters task information
  ↓
Input is validated
  ↓
A unique ID is generated
  ↓
Status and created_at are assigned
  ↓
Task is added to the in-memory list
  ↓
Success message is displayed

## 9.Components

The application will be divided into the following logical components:

### CLI / Input
Responsible for displaying the menu and collecting input from the user.

### Task Management
Responsible for performing task operations such as create, get, update, delete, complete, and search.

### Task Storage
Responsible for storing tasks in an in-memory list.

### Validation
Responsible for checking user input and preventing invalid operations.

### Output
Responsible for displaying task information, success messages, and error messages to the user.

## 10.Task Operations

### Create Task
- Ask for the title.
- Ask for an optional description.
- Generate the next unique ID.
- Set status to `in_progress`.
- Generate `created_at`.
- Add the task to the task list.

### List Tasks
- Display all tasks.
- If there are no tasks, display "No tasks found."

### Get Task
- Ask for the task ID.
- Find the task with that ID.
- Display all task information.
- If the ID does not exist, display "Task not found."

### Update Task
- Ask for the task ID.
- Display the current task information.
- Allow the user to update the title, description or status.
- Keep the task ID unchanged.

### Delete Task
- Ask for the task ID.
- Display the task or confirm that it exists.
- Ask the user for confirmation.
- Delete the task only if the user confirms.

### Complete Task
- Ask for the task ID.
- Change the task status to `completed`.
- If the task does not exist, display an error message.

### Search Tasks
- Ask for a search term.
- Search both title and description.
- Display all matching tasks.
- If there are no matches, display "No tasks found."

## 11.Design Assumptions

The following assumptions are used for Version 1:

- The application is used by one user at a time.
- Tasks are stored only in memory.
- Task data is lost when the application terminates.
- Task IDs are generated automatically.
- Task IDs are not reused after deletion.
- Title is required.
- Description is optional.
- Status can be `pending`, `in_progress`, or `completed`.
- The user cannot change a task's ID.

## 12.Future Evolution

Version 1 is intentionally kept simple and uses in-memory storage.

Future versions could evolve the system by adding persistent storage, SQL, APIs, backend frameworks, authentication, deployment, distributed systems and eventually AI capabilities.

These features are outside the scope of Version 1.

## 13.Summary

Version 1 will be a simple Python CLI Task Manager using an in-memory list.

The system will provide create, list, get, update, delete, complete and search operations.

The design focuses on clear input validation, simple task management logic, readable output and handling of edge cases.