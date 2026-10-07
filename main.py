from src.task_manager import TaskManager
from src.auth import AuthManager


def display_task(task):
    print(f"\nID: {task.id}")
    print(f"Title: {task.title}")
    print(f"Description: {task.description}")
    print(f"Status: {task.status}")
    print(f"Created At: {task.created_at}")


def display_tasks(tasks):
    if not tasks:
        print("\nNo tasks found.")
        return

    for task in tasks:
        display_task(task)


def get_task_id():
    while True:
        value = input("Enter task ID: ").strip()

        try:
            return int(value)
        except ValueError:
            print("Invalid task ID. Please enter a number.")


def task_menu(manager, user):
    while True:
        print("\n===== NATRAYO TASK MANAGER =====")
        print(f"Logged in as: {user['username']}")
        print("1. Create Task")
        print("2. List All Tasks")
        print("3. Get Task")
        print("4. Update Task")
        print("5. Delete Task")
        print("6. Complete Task")
        print("7. Search Tasks")
        print("8. Logout")

        choice = input("Enter your choice: ").strip()

        if choice == "1":
            title = input("Enter task title: ").strip()

            if not title:
                print("Title cannot be empty.")
                continue

            description = input("Enter task description: ").strip()

            try:
                task = manager.create_task(title, description)
                print("\nTask created successfully.")
                display_task(task)
            except ValueError as error:
                print(f"Error: {error}")

        elif choice == "2":
            display_tasks(manager.list_tasks())

        elif choice == "3":
            task_id = get_task_id()
            task = manager.get_task(task_id)

            if task is None:
                print("Task not found.")
            else:
                display_task(task)

        elif choice == "4":
            task_id = get_task_id()
            task = manager.get_task(task_id)

            if task is None:
                print("Task not found.")
                continue

            print("\nCurrent task:")
            display_task(task)

            print("\nEnter new information.")
            print("Press Enter to keep the current value.")

            title = input(f"Title [{task.title}]: ").strip()
            description = input(
                f"Description [{task.description}]: "
            ).strip()
            status = input(
                f"Status [{task.status}]: "
            ).strip().lower()

            new_title = title if title else None
            new_description = description if description else None
            new_status = status if status else None

            try:
                updated_task = manager.update_task(
                    task_id,
                    title=new_title,
                    description=new_description,
                    status=new_status,
                )

                print("\nTask updated successfully.")
                display_task(updated_task)

            except ValueError as error:
                print(f"Error: {error}")

        elif choice == "5":
            task_id = get_task_id()
            task = manager.get_task(task_id)

            if task is None:
                print("Task not found.")
                continue

            display_task(task)

            confirmation = input(
                "Are you sure you want to delete this task? (y/n): "
            ).strip().lower()

            if confirmation == "y":
                manager.delete_task(task_id)
                print("Task deleted successfully.")
            else:
                print("Delete cancelled.")

        elif choice == "6":
            task_id = get_task_id()
            task = manager.complete_task(task_id)

            if task is None:
                print("Task not found.")
            else:
                print("Task marked as completed.")
                display_task(task)

        elif choice == "7":
            keyword = input("Enter search term: ").strip()

            results = manager.search_tasks(keyword)
            display_tasks(results)

        elif choice == "8":
            print("Logged out successfully.")
            break

        else:
            print("Invalid choice. Please select an option from 1 to 8.")


def main():
    auth = AuthManager()

    while True:
        print("\n===== NATRAYO =====")
        print("1. Signup")
        print("2. Login")
        print("3. Exit")

        choice = input("Enter your choice: ").strip()

        if choice == "1":
            username = input("Enter username: ").strip()
            password = input("Enter password: ")

            try:
                user_id = auth.signup(username, password)
                print(f"Signup successful. Your user ID is {user_id}.")
            except ValueError as error:
                print(f"Signup failed: {error}")

        elif choice == "2":
            username = input("Enter username: ").strip()
            password = input("Enter password: ")

            user = auth.login(username, password)

            if user is None:
                print("Invalid username or password.")
            else:
                print(f"\nLogin successful. Welcome, {user['username']}!")

                manager = TaskManager(user["id"])
                task_menu(manager, user)

        elif choice == "3":
            print("Exiting NATRAYO.")
            break

        else:
            print("Invalid choice. Please select 1, 2, or 3.")


if __name__ == "__main__":
    main()