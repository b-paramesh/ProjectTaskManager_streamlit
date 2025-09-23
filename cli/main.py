from service.user_service import UserService
from service.task_service import TaskService
from service.assignment_service import AssignmentService

def main():
    while True:
        print("\n--- Task Management CLI ---")
        print("1. Add User")
        print("2. Edit User")
        print("3. Delete User")
        print("4. Add Task")
        print("5. Edit Task")
        print("6. Delete Task")
        print("7. Assign Task")
        print("8. Update Task Status")
        print("9. List Tasks")
        print("0. Exit")
        choice = input("Enter choice: ")

        # ---------------- Add User ----------------
        if choice == "1":
            username = input("Username: ")
            email = input("Email: ")
            password = input("Password: ")
            UserService.create_user(username, email, password)
            print("User added successfully!")

        # ---------------- Edit User ----------------
        elif choice == "2":
            valid_fields = ["username", "email", "password_hash"]
            user_id = int(input("User ID: "))
            field = input(f"Field to edit ({'/'.join(valid_fields)}): ").strip()
            if field not in valid_fields:
                print("Invalid field name! Try again.")
                continue
            value = input("New value: ")
            UserService.update_user(user_id, **{field: value})
            print("User updated successfully!")

        # ---------------- Delete User ----------------
        elif choice == "3":
            user_id = int(input("User ID: "))
            UserService.remove_user(user_id)
            print("User deleted successfully!")

        # ---------------- Add Task ----------------
        elif choice == "4":
            title = input("Task Title: ")
            description = input("Task Description: ")
            deadline = input("Deadline (YYYY-MM-DD) or leave blank: ") or None
            TaskService.create_task(title, description, deadline=deadline)
            print("Task added successfully!")

        # ---------------- Edit Task ----------------
        elif choice == "5":
            valid_task_fields = ["title", "description", "status", "deadline"]
            task_id = int(input("Task ID: "))
            field = input(f"Field to edit ({'/'.join(valid_task_fields)}): ").strip()
            if field not in valid_task_fields:
                print("Invalid field name! Try again.")
                continue
            value = input("New value: ")
            TaskService.update_task(task_id, **{field: value})
            print("Task updated successfully!")

        # ---------------- Delete Task ----------------
        elif choice == "6":
            task_id = int(input("Task ID: "))
            TaskService.delete_task(task_id)
            print("Task deleted successfully!")

        # ---------------- Assign Task ----------------
        elif choice == "7":
            task_id = int(input("Task ID: "))
            user_id = int(input("User ID: "))
            AssignmentService.assign_task(task_id, user_id)
            print("Task assigned successfully!")

        # ---------------- Update Task Status ----------------
        elif choice == "8":
            task_id = int(input("Task ID: "))
            status = input("New Status (pending/in-progress/completed): ")
            if status not in ["pending", "in-progress", "completed"]:
                print("Invalid status! Try again.")
                continue
            TaskService.change_status(task_id, status)
            print("Task status updated successfully!")

        # ---------------- List Tasks ----------------
        elif choice == "9":
            filter_by = input("Filter by (user_id/status/deadline) or leave blank: ") or None
            if filter_by not in ("user_id", "status", "deadline", None):
                print("Invalid filter field. Ignoring filter.")
                filter_by = None
            value = input("Filter value or leave blank: ") or None
            tasks = TaskService.list_tasks(filter_by, value)
            for t in tasks:
                print(t)

        # ---------------- Exit ----------------
        elif choice == "0":
            print("Exiting...")
            break

        else:
            print("Invalid choice! Try again.")

if __name__ == "__main__":
    main()
