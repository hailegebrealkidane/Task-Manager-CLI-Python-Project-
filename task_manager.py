from storage import load_tasks, save_tasks


class TaskManager:
    def __init__(self):
        self.tasks = load_tasks()

    def view_tasks(self):
        if not self.tasks:
            print("No tasks found.")
            return

        for i, task in enumerate(self.tasks):
            status = "✔" if task["done"] else "✘"
            print(f"{i+1}. [{status}] {task['title']}")

    def add_task(self, title):
        self.tasks.append({"title": title, "done": False})
        save_tasks(self.tasks)
        print("Task added!")

    def complete_task(self, index):
        if 0 <= index < len(self.tasks):
            self.tasks[index]["done"] = True
            save_tasks(self.tasks)
            print("Task completed!")
        else:
            print("Invalid task number")

    def delete_task(self, index):
        if 0 <= index < len(self.tasks):
            self.tasks.pop(index)
            save_tasks(self.tasks)
            print("Task deleted!")
        else:
            print("Invalid task number")
