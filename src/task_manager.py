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

    def list_tasks(self):
        return self.tasks

    def get_task(self, task_id):
        for task in self.tasks:
            if task.id == task_id:
                return task

        return None

    def update_task(self, task_id, title=None, description=None, status=None):
        task = self.get_task(task_id)

        if task is None:
            return None

        if title is not None:
            if not title.strip():
                raise ValueError("Title cannot be empty.")
            task.title = title.strip()

        if description is not None:
            task.description = description.strip()

        if status is not None:
            if status not in ["pending", "in_progress", "completed"]:
                raise ValueError("Invalid status.")
            task.status = status

        return task

    def delete_task(self, task_id):
        task = self.get_task(task_id)

        if task is None:
            return None

        self.tasks.remove(task)
        return task

    def complete_task(self, task_id):
        task = self.get_task(task_id)

        if task is None:
            return None

        task.status = "completed"
        return task

    def search_tasks(self, keyword):
        keyword = keyword.strip().lower()

        if not keyword:
            return []

        return [
            task
            for task in self.tasks
            if keyword in task.title.lower()
            or keyword in task.description.lower()
        ]