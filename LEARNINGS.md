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

---

## 2. Requirements vs Design Decisions

A requirement describes **what the system must do**.

A design decision describes **how we choose to implement it**.

Example:

Requirement:

- Every task must have a unique ID.

Design decision:

- Generate sequential integer IDs starting from 1.

Another example:

Requirement:

- Tasks must be searchable.

Design decision:

- Search the task title and description using case-insensitive text matching.

---

## 3. CLI

CLI means **Command-Line Interface**.

It allows the user to interact with the application by entering commands or choosing options through the terminal.

This project uses a CLI instead of a web interface.

The CLI is responsible for:

- Displaying the menu.
- Reading user input.
- Calling the appropriate task management operation.
- Displaying results and error messages.

---

## 4. In-Memory Storage

Version 1 stores tasks in memory using a Python list.

This means:

- Tasks can be created and managed while the program is running.
- No database is required.
- Tasks are lost when the program exits.

A list was chosen because Version 1 is a small CLI application and does not require persistent storage.

---

## 5. Validation

Validation checks whether user input is acceptable before performing an operation.

Examples:

- Empty title should be rejected.
- Invalid task ID should be handled.
- Invalid status should be rejected.
- Invalid menu choices should be handled.

Validation helps prevent invalid data from entering the task management logic.

---

## 6. Edge Cases

An edge case is an unusual situation that the program must handle correctly.

Examples:

- No tasks exist.
- A task ID does not exist.
- Search returns no results.
- User enters an empty title.
- User enters an invalid status.
- User cancels a delete operation.
- User enters an invalid menu choice.

Testing these cases helped verify that the application does not fail during normal invalid input.

---

## 7. Git and Version Control

Git is used to track changes in the project.

Important Git concepts used in this project include:

- Working directory
- Staging area
- Commit
- Branch
- Merge
- Remote repository
- Pull Request

The project uses descriptive commit messages that clearly explain what changed.

A separate feature branch was used for task-management functionality before merging the work into `master`.

---

## 8. Testing and Debugging

The application was tested after implementation.

The process included:

1. Run the application.
2. Test normal operations.
3. Test edge cases.
4. Identify failures.
5. Investigate the cause.
6. Fix the problem.
7. Run the relevant test again.
8. Document important bugs and fixes.

Three debugging cases were recorded in `BUGS_AND_DEBUGGING.md`.

These included:

- Empty task title validation.
- Using a manager variable that was not defined in a new Python session.
- Testing an updated class before restarting the Python session.

---

## 9. What Was Easiest?

The basic task operations were easier to understand after separating the `Task` model from the `TaskManager` logic.

Creating, listing, updating, completing, deleting, and searching tasks became easier once each operation had a clear responsibility.

---

## 10. What Was Hardest?

The hardest part was understanding the complete development workflow rather than only writing the Python code.

This included understanding:

- Git branches.
- Staging and commits.
- Remote repositories.
- Pushing branches.
- Merging branches.
- Debugging failures.
- Testing edge cases.

---

## 11. What Became Clear After Implementation?

The difference between requirements and implementation became clearer.

For example:

The requirement is:

- The user should be able to search tasks.

The implementation decision is:

- Search the title and description using case-insensitive matching.

The project also showed why separating CLI code from task-management logic makes the code easier to understand and test.

---

## 12. What Happens With a Very Large Number of Tasks?

Version 1 stores all tasks in a Python list.

As the number of tasks becomes very large:

- Searching requires checking many tasks.
- Updating and finding tasks by ID require scanning the list.
- Memory usage increases.

A database with indexes would be more appropriate for a larger application.

---

## 13. What Would I Change With Another Day?

With more development time, I would consider:

- Persistent storage using a database.
- Better automated tests.
- More structured validation.
- A REST API.
- Better search functionality.
- More detailed error handling.

These improvements are outside the scope of the Version 1 CLI implementation.

---

## 14. What Abstraction Did I Avoid?

I avoided adding unnecessary frameworks and abstractions in Version 1.

The application uses simple Python classes and a list because the current requirements do not need a web framework, database, or AI framework.

Keeping Version 1 simple makes the core task-management logic easier to understand.

---

## 15. What Did I Use AI For?

AI was used as a development and learning assistant.

It helped with:

- Understanding requirements.
- Discussing design decisions.
- Explaining Git commands and workflows.
- Debugging errors.
- Reviewing implementation ideas.
- Creating documentation drafts.
- Identifying edge cases and testing scenarios.

The generated suggestions were checked by running the code and verifying the results.

---

## 16. What Do I Not Understand Yet?

Some areas that require further learning include:

- Designing a production-ready database schema.
- Building a REST API around the task-management logic.
- Automated testing at a larger scale.
- Production deployment and monitoring.

These are possible future learning areas beyond Version 1.

---

## 17. How Would I Turn This Into a REST API?

The existing task-management logic could be reused behind an API layer.

For example:

- `POST /tasks` — create a task.
- `GET /tasks` — list tasks.
- `GET /tasks/{id}` — get a task.
- `PUT /tasks/{id}` — update a task.
- `DELETE /tasks/{id}` — delete a task.
- `POST /tasks/{id}/complete` — complete a task.
- `GET /tasks/search` — search tasks.

A web framework such as FastAPI could handle HTTP requests while the existing task-management logic would handle the actual operations.

---

## 18. Main Engineering Learning

The main learning from this project is that software development is not only about writing code.

The process includes:

- Understanding requirements.
- Making design decisions.
- Planning architecture.
- Implementing features.
- Testing.
- Debugging.
- Using version control.
- Documenting the work.
- Explaining and defending design decisions.