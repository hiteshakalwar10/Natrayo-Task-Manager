from .task import Task
from .database import get_connection


class TaskManager:
    def __init__(self, user_id):
        self.connection = get_connection()
        self.user_id = user_id

    def create_task(self, title, description=""):
        if not title.strip():
            raise ValueError("Title cannot be empty.")

        cursor = self.connection.cursor()

        query = """
            INSERT INTO tasks (title, description, status, user_id)
            VALUES (%s, %s, %s, %s)
        """

        values = (
            title.strip(),
            description.strip(),
            "in_progress",
            self.user_id,
        )

        cursor.execute(query, values)
        self.connection.commit()

        task_id = cursor.lastrowid

        cursor.close()

        return self.get_task(task_id)

    def list_tasks(self):
        cursor = self.connection.cursor()

        query = """
            SELECT id, title, description, status, created_at
            FROM tasks
            WHERE user_id = %s
        """

        cursor.execute(query, (self.user_id,))

        rows = cursor.fetchall()

        cursor.close()

        tasks = []

        for row in rows:
            task = Task(row[0], row[1], row[2])
            task.status = row[3]
            task.created_at = row[4]
            tasks.append(task)

        return tasks

    def get_task(self, task_id):
        cursor = self.connection.cursor()

        query = """
            SELECT id, title, description, status, created_at
            FROM tasks
            WHERE id = %s AND user_id = %s
        """

        cursor.execute(query, (task_id, self.user_id))

        row = cursor.fetchone()

        cursor.close()

        if row is None:
            return None

        task = Task(row[0], row[1], row[2])
        task.status = row[3]
        task.created_at = row[4]

        return task

    def update_task(self, task_id, title=None, description=None, status=None):
        task = self.get_task(task_id)

        if task is None:
            return None

        if title is not None:
            if not title.strip():
                raise ValueError("Title cannot be empty.")
            title = title.strip()

        if description is not None:
            description = description.strip()

        if status is not None:
            if status not in ["pending", "in_progress", "completed"]:
                raise ValueError("Invalid status.")

        cursor = self.connection.cursor()

        query = """
            UPDATE tasks
            SET title = %s,
                description = %s,
                status = %s
            WHERE id = %s AND user_id = %s
        """

        new_title = title if title is not None else task.title
        new_description = (
            description if description is not None else task.description
        )
        new_status = status if status is not None else task.status

        values = (
            new_title,
            new_description,
            new_status,
            task_id,
            self.user_id,
        )

        cursor.execute(query, values)
        self.connection.commit()

        cursor.close()

        return self.get_task(task_id)

    def delete_task(self, task_id):
        task = self.get_task(task_id)

        if task is None:
            return None

        cursor = self.connection.cursor()

        query = """
            DELETE FROM tasks
            WHERE id = %s AND user_id = %s
        """

        cursor.execute(query, (task_id, self.user_id))
        self.connection.commit()

        cursor.close()

        return task

    def complete_task(self, task_id):
        task = self.get_task(task_id)

        if task is None:
            return None

        cursor = self.connection.cursor()

        query = """
            UPDATE tasks
            SET status = %s
            WHERE id = %s AND user_id = %s
        """

        cursor.execute(
            query,
            ("completed", task_id, self.user_id),
        )

        self.connection.commit()

        cursor.close()

        return self.get_task(task_id)

    def search_tasks(self, keyword):
        keyword = keyword.strip().lower()

        if not keyword:
            return []

        cursor = self.connection.cursor()

        query = """
            SELECT id, title, description, status, created_at
            FROM tasks
            WHERE user_id = %s
              AND (
                  LOWER(title) LIKE %s
                  OR LOWER(description) LIKE %s
              )
        """

        search_value = "%" + keyword + "%"

        cursor.execute(
            query,
            (self.user_id, search_value, search_value),
        )

        rows = cursor.fetchall()

        cursor.close()

        tasks = []

        for row in rows:
            task = Task(row[0], row[1], row[2])
            task.status = row[3]
            task.created_at = row[4]
            tasks.append(task)

        return tasks