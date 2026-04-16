from task_manager import TaskManager


def main():
    manager = TaskManager()

    while True:
        print("\nTask Manager")
        print("1. View Tasks")
        print("2. Add Task")
        print("3. Complete Task")
        print("4. Delete Task")
        print("5. Exit")

        choice = input("Choose an option: ")

        if choice == "1":
            manager.view_tasks()
        elif choice == "2":
            title = input("Enter task title: ")
            manager.add_task(title)
        elif choice == "3":
            index = int(input("Enter task number to complete: "))
            manager.complete_task(index - 1)
        elif choice == "4":
            index = int(input("Enter task number to delete: "))
            manager.delete_task(index - 1)
        elif choice == "5":
            break
        else:
            print("Invalid choice")


if __name__ == "__main__":
    main()
