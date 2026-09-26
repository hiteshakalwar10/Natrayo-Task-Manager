from datetime import datetime


class Task:
    def __init__(self, task_id, title, description):
        self.id = task_id
        self.title = title
        self.description = description
        self.status = "in_progress"
        self.created_at = datetime.now()