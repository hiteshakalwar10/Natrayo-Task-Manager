import unittest

from src.task_manager import TaskManager


class TestTaskManager(unittest.TestCase):

    def test_create_task(self):
        manager = TaskManager()

        task = manager.create_task(
            "Learn Python",
            "Practice Python programming"
        )

        self.assertEqual(task.id, 1)
        self.assertEqual(task.title, "Learn Python")
        self.assertEqual(task.description, "Practice Python programming")
        self.assertEqual(task.status, "in_progress")

    def test_empty_title(self):
        manager = TaskManager()

        with self.assertRaises(ValueError):
            manager.create_task("", "Test description")

    def test_get_task(self):
        manager = TaskManager()
        manager.create_task("Learn Python")

        task = manager.get_task(1)

        self.assertIsNotNone(task)
        self.assertEqual(task.title, "Learn Python")

    def test_update_task(self):
        manager = TaskManager()
        manager.create_task("Learn Python")

        task = manager.update_task(
            1,
            title="Learn Git",
            description="Practice Git commands",
            status="completed"
        )

        self.assertEqual(task.title, "Learn Git")
        self.assertEqual(task.description, "Practice Git commands")
        self.assertEqual(task.status, "completed")

    def test_delete_task(self):
        manager = TaskManager()
        manager.create_task("Test Task")

        deleted = manager.delete_task(1)

        self.assertIsNotNone(deleted)
        self.assertIsNone(manager.get_task(1))
        self.assertEqual(len(manager.list_tasks()), 0)

    def test_complete_task(self):
        manager = TaskManager()
        manager.create_task("Complete Task")

        task = manager.complete_task(1)

        self.assertEqual(task.status, "completed")

    def test_search_tasks(self):
        manager = TaskManager()
        manager.create_task(
            "Learn Python",
            "Practice Python programming"
        )
        manager.create_task(
            "Learn Git",
            "Practice Git commands"
        )

        results = manager.search_tasks("python")

        self.assertEqual(len(results), 1)
        self.assertEqual(results[0].title, "Learn Python")

    def test_nonexistent_task(self):
        manager = TaskManager()

        self.assertIsNone(manager.get_task(999))
        self.assertIsNone(manager.update_task(999, title="Test"))
        self.assertIsNone(manager.delete_task(999))
        self.assertIsNone(manager.complete_task(999))


if __name__ == "__main__":
    unittest.main()