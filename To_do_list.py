class Task:
    def __init__(self, title, description, due_date):
        self.title = title
        self.description = description
        self.due_date = due_date
        self.completed = False

class TodoList:
    def __init__(self):
        self.tasks = []

    def add_task(self, task):
        self.tasks.append(task)

    def remove_task(self, task_title):
        self.tasks = [task for task in self.tasks if task.title != task_title]

    def list_tasks(self):
        for idx, task in enumerate(self.tasks, start=1):
            status = "Completed" if task.completed else "Pending"
            print(f"{idx}. [{status}] {task.title} - {task.description} (Due: {task.due_date})")

def main():
    todo_list = TodoList()

    while True:
        print("\nTODO LIST MENU:")
        print("1. Add Task")
        print("2. Remove Task")
        print("3. List Tasks")
        print("4. Quit")

        choice = input("Enter your choice: ")

        if choice == "1":
            title = input("Enter task title: ")
            description = input("Enter task description: ")
            due_date = input("Enter due date (YYYY-MM-DD): ")
            todo_list.add_task(Task(title, description, due_date))
            print("Task added successfully!")
        elif choice == "2":
            title = input("Enter title of task to remove: ")
            todo_list.remove_task(title)
            print("Task removed successfully!")
        elif choice == "3":
            todo_list.list_tasks()
        elif choice == "4":
            print("Exiting...")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
