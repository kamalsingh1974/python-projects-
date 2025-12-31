import json
import os

FILENAME = "todo_list.json"


def load_tasks():
    """Loads tasks from the JSON file. Creates an empty list if file doesn't exist."""
    if not os.path.exists(FILENAME):
        return []
    try:
        with open(FILENAME, 'r') as file:
            return json.load(file)
    except (json.JSONDecodeError, IOError):
        return []


def save_tasks(tasks):
    """Saves the current task list to the JSON file."""
    with open(FILENAME, 'w') as file:
        json.dump(tasks, file, indent=4)


def add_task(tasks):
    title = input("Enter the task description: ").strip()
    if title:
        tasks.append({"task": title, "done": False})
        save_tasks(tasks)
        print("Task added!")


def view_tasks(tasks):
    if not tasks:
        print("\nYour list is empty.")
        return

    print("\n--- YOUR TO-DO LIST ---")
    for index, item in enumerate(tasks, start=1):
        status = "✅" if item["done"] else "❌"
        print(f"{index}. {item['task']} [{status}]")


def mark_done(tasks):
    view_tasks(tasks)
    try:
        task_num = int(input("\nEnter the task number to mark as done: "))
        tasks[task_num - 1]["done"] = True
        save_tasks(tasks)
        print("Task updated!")
    except (ValueError, IndexError):
        print("Error: Invalid task number.")


def delete_task(tasks):
    view_tasks(tasks)
    try:
        task_num = int(input("\nEnter the task number to delete: "))
        removed = tasks.pop(task_num - 1)
        save_tasks(tasks)
        print(f"Deleted: {removed['task']}")
    except (ValueError, IndexError):
        print("Error: That task number does not exist.")


def main():
    tasks = load_tasks()
    while True:
        print("\n1. View  2. Add  3. Complete  4. Delete  5. Exit")
        choice = input("Choose an option: ")

        if choice == '1':
            view_tasks(tasks)
        elif choice == '2':
            add_task(tasks)
        elif choice == '3':
            mark_done(tasks)
        elif choice == '4':
            delete_task(tasks)
        elif choice == '5':
            break
        else:
            print("Invalid choice.")


if __name__ == "__main__":
    main()