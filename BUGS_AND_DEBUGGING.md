# NATRAYO Task Manager — Bugs and Debugging

## 1. Purpose

This document records deliberate failures and debugging work performed during development.

For each failure, the expected behavior, actual behavior, reproduction steps, investigation, root cause, fix, verification, and prevention are recorded.

---

## 2. Bug 1 — Empty Task Title

### What did I expect?

Creating a task with an empty title should be rejected because the task title is required.

### What actually happened?

The application raised:

```text
ValueError: Title cannot be empty.
```

This was the expected validation behavior.

### How did I reproduce it?

I ran:

```python
manager.create_task("", "Test")
```

The application produced:

```text
ValueError: Title cannot be empty.
```

### First hypothesis

The task creation logic should validate the title before creating the task.

### Evidence inspected

The error message showed that `create_task()` was checking whether the title was empty.

### Root cause

An empty title was intentionally rejected by the validation logic.

### What change fixed it?

The validation was kept in `create_task()`:

```python
if not title.strip():
    raise ValueError("Title cannot be empty.")
```

### How did I verify the fix?

I tested a valid task after the failure:

```python
manager.create_task("Learn Python", "Practice Python programming")
```

The task was created successfully.

### How can the problem be prevented?

Validate required input before creating the task.

---

## 3. Bug 2 — Manager Variable Not Defined

### What did I expect?

I expected to be able to call:

```python
manager.search_tasks("python")
```

and receive matching tasks.

### What actually happened?

Python returned:

```text
NameError: name 'manager' is not defined
```

### How did I reproduce it?

I started a new Python session and immediately ran:

```python
manager.search_tasks("python")
```

### First hypothesis

The `manager` object had not been created in the current Python session.

### Evidence inspected

The error was:

```text
NameError: name 'manager' is not defined
```

This means Python did not have a variable named `manager` in the current session.

### Root cause

The previous Python session had been closed, so the variable created in that session no longer existed.

### What change fixed it?

I imported `TaskManager` and created a new manager object:

```python
from src.task_manager import TaskManager
manager = TaskManager()
```

### How did I verify the fix?

I created tasks and successfully used:

```python
manager.search_tasks("python")
```

The search returned the expected task.

### How can the problem be prevented?

When starting a new Python session, initialize the required objects before using them.

---

## 4. Bug 3 — search_tasks() Not Available

### What did I expect?

I expected:

```python
manager.search_tasks("python")
```

to search the tasks.

### What actually happened?

Python returned:

```text
AttributeError: 'TaskManager' object has no attribute 'search_tasks'
```

### How did I reproduce it?

I created a `TaskManager` object and called:

```python
results = manager.search_tasks("python")
```

The method was not available in the loaded class.

### First hypothesis

The `search_tasks()` method might not have been added to `TaskManager`, or Python might still be using an older version of the file.

### Evidence inspected

I checked `src/task_manager.py` and verified that the `search_tasks()` method existed.

The running Python session was still using the older loaded version of the class.

### Root cause

The Python session had loaded an older version of `TaskManager` before `search_tasks()` was added.

Saving the source file did not automatically reload the already-running Python session.

### What change fixed it?

I exited the Python session and started a new one so that the latest `task_manager.py` was loaded.

I then checked:

```python
print(hasattr(TaskManager, "search_tasks"))
```

The result was:

```text
True
```

### How did I verify the fix?

I created test tasks and ran:

```python
results = manager.search_tasks("python")
```

The search returned:

```text
[(1, 'Learn Python')]
```

I also tested a word from a task description and confirmed that description searching worked.

### How can the problem be prevented?

After making changes to a Python module, restart the Python session when testing the updated class.

---

## 5. Debugging Process

The following process was used during debugging:

1. Reproduce the failure.
2. Identify the expected behavior.
3. Identify the actual behavior.
4. Form a hypothesis.
5. Inspect evidence.
6. Identify the root cause.
7. Apply the fix.
8. Run the relevant test again.
9. Check that the fix did not introduce another problem.

---

## 6. Testing and Debugging

Testing included:

- Creating a valid task.
- Creating a task with an empty title.
- Creating multiple tasks.
- Retrieving an existing task.
- Retrieving a nonexistent task.
- Updating an existing task.
- Deleting a task with confirmation.
- Completing a task.
- Searching by title.
- Searching by description.
- Searching with no matching results.
- Invalid task IDs.
- Invalid menu choices.
- Starting a new Python session.
- Verifying updated Python code after restarting the session.

---

## 7. Lessons From Debugging

The debugging process showed that:

- Validation should happen before creating or updating data.
- Python variables exist only in the current running session.
- Changes to a Python module may require restarting the Python session before testing.
- Error messages provide useful evidence for identifying the type of failure.
- A failure should be reproduced and investigated before changing code.