import json
from datetime import datetime

class ToDoList:
    def __init__(self):
        self.tasks = []

    def load_tasks(self):
        try:
            with open("tasks.json", "r") as file:
                self.tasks = json.load(file)
        except FileNotFoundError:
            pass

    def save_tasks(self):
        with open("tasks.json", "w") as file:
            json.dump(self.tasks, file, indent=2)

    def show_tasks(self):
        if not self.tasks:
            print("No tasks found.")
        else:
            for index, task in enumerate(self.tasks, start=1):
                print(f"{index}. {task['title']} - {task['date']}")

    def add_task(self, title, date):
        task = {"title": title, "date": date}
        self.tasks.append(task)
        self.save_tasks()
        print("Task added successfully.")

    def update_task(self, index, new_title, new_date):
        if 1 <= index <= len(self.tasks):
            self.tasks[index - 1]["title"] = new_title
            self.tasks[index - 1]["date"] = new_date
            self.save_tasks()
            print("Task updated successfully.")
        else:
            print("Invalid task index.")

    def delete_task(self, index):
        if 1 <= index <= len(self.tasks):
            del self.tasks[index - 1]
            self.save_tasks()
            print("Task deleted successfully.")
        else:
            print("Invalid task index.")


def main():
    todo_list = ToDoList()
    todo_list.load_tasks()

    while True:
        print("\nTODO LIST APPLICATION")
        print("1. Show Tasks")
        print("2. Add Task")
        print("3. Update Task")
        print("4. Delete Task")
        print("5. Exit")

        choice = input("Enter your choice (1-5): ")

        if choice == "1":
            todo_list.show_tasks()
        elif choice == "2":
            title = input("Enter task title: ")
            date = input("Enter task due date (YYYY-MM-DD): ")
            todo_list.add_task(title, date)
        elif choice == "3":
            index = int(input("Enter the index of the task to update: "))
            new_title = input("Enter the new task title: ")
            new_date = input("Enter the new task due date (YYYY-MM-DD): ")
            todo_list.update_task(index, new_title, new_date)
        elif choice == "4":
            index = int(input("Enter the index of the task to delete: "))
            todo_list.delete_task(index)
        elif choice == "5":
            todo_list.save_tasks()
            print("Exiting the TODO List application. Goodbye!")
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 5.")

if __name__ == "__main__":
    main()
