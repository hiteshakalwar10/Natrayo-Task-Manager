from .task import Task


class TaskManager:
    def __init__(self):
        self.tasks = []
        self.next_id = 1

    def create_task(self, title, description=""):
        if not title.strip():
            raise ValueError("Title cannot be empty.")

        task = Task(self.next_id, title.strip(), description.strip())
        self.tasks.append(task)
        self.next_id += 1

        return task