import os
import json


class Task:
    def __init__(self, title, status="incomplete", priority="normal"):
        self.title = title
        self.status = status
        self.priority = priority

    def __str__(self):
        return f"[{self.status}] {self.title} (Priority: {self.priority})"

    def mark_complete(self):
        self.status = "complete"

# create todo list fictionality


class TodoList:
    def __init__(self):
        self.tasks = []
        self.load_tasks()

    def add_task(self, task):
        self.tasks.append(task)
        print(f"Added task: {task.title}")

    def view_tasks(self):
        if not self.tasks:
            print("no task in your to-do list.")
        else:
            for i, task in enumerate(self.tasks):
                print(f"{i + 1}. {task}")

    def delete_task(self, index):
        if 0 <= index < len(self.tasks):
            removed_task = self.tasks.pop(index)
            print(f"Deleted task: {removed_task.title}")
        else:
            print("invalid task number")

    def mark_task_complete(self, index):
        if 0 <= index < len(self.tasks):
            self.tasks[index].mark_complete()
            print(f"marked task as complete: {self.tasks[index].title}")
        else:
            print("invalid task number")

    def save_tasks(self):
        with open("task.json", "w") as file:
            tasks_data = [{'title': task.title, 'status': task.status,
                           'priority': task.priority} for task in self.tasks]
            json.dump(tasks_data, file)
        print("Tasks saved to tasks.json")

    def load_tasks(self):
        if os.path.exists("tasks.json"):
            with open("tasks.json", "r") as file:
                tasks_data = json.load(file)
                for task_data in tasks_data:
                    task = Task(
                        task_data['title'], task_data['status'], task_data['priority'])
                    self.tasks.append(task)
            print("Tasks loaded from tasks.json")
        else:
            print("no saved tasks found")

# CLI menu implementation


def display_menu():
    print("\nTo-Do List CLI")
    print("1. Add Task")
    print("2. View Tasks")
    print("3. Mark task as complete")
    print("4. Delete task")
    print("5. Save Tasks")
    print("6. Exit")


def main():
    todo_list = TodoList()

    while True:
        display_menu()
        choice = input("Enter your choice (1-6): ")

        if choice == "1":
            title = input("Enter task title: ")
            priority = input(
                "Enter task priority (low, normal, high): ").lower()
            task = Task(title, priority=priority)
            todo_list.add_task(task)

        elif choice == "2":
            todo_list.view_tasks()

        elif choice == "3":
            todo_list.view_tasks()
            task_num = int(input("Enter a number to mark complete: ")) - 1
            todo_list.mark_task_complete(task_num)

        elif choice == "4":
            todo_list.view_tasks()
            task_num = int(input("Enter task number to delete: ")) - 1
            todo_list.delete_task(task_num)

        elif choice == "5":
            todo_list.save_tasks()

        elif choice == "6":
            todo_list.save_tasks()
            print("Goodbye!")
            break

        else:
            print("Invalid choice. please try again.")


if __name__ == "__main__":
    main()
