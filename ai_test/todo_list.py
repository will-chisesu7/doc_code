import json
import os
from datetime import datetime

TASKS_FILE = "tasks.json"


def load_tasks():
    if os.path.exists(TASKS_FILE):
        with open(TASKS_FILE, "r") as f:
            return json.load(f)
    return []


def save_tasks(tasks):
    with open(TASKS_FILE, "w") as f:
        json.dump(tasks, f, indent=4)


def view_tasks(tasks):
    print("\n" + "=" * 50)
    print("              YOUR TASKS")
    print("=" * 50)
    if not tasks:
        print("  No tasks yet.")
    else:
        for i, task in enumerate(tasks, start=1):
            status = "✓" if task["done"] else "✗"
            print(f"  {i}. [{status}] {task['task']} (Added: {task['added']})")
    print("=" * 50)


def add_task(tasks):
    task = input("Enter task: ").strip()
    if not task:
        print("Task cannot be empty.")
        return
    tasks.append({"task": task, "done": False, "added": datetime.now().strftime("%Y-%m-%d %H:%M")})
    save_tasks(tasks)
    print(f"Task '{task}' added.")


def complete_task(tasks):
    view_tasks(tasks)
    if not tasks:
        return
    try:
        num = int(input("Enter task number to mark complete: "))
        if 1 <= num <= len(tasks):
            tasks[num - 1]["done"] = True
            save_tasks(tasks)
            print(f"Task '{tasks[num - 1]['task']}' marked as complete.")
        else:
            print("Invalid task number.")
    except ValueError:
        print("Please enter a valid number.")


def delete_task(tasks):
    view_tasks(tasks)
    if not tasks:
        return
    try:
        num = int(input("Enter task number to delete: "))
        if 1 <= num <= len(tasks):
            removed = tasks.pop(num - 1)
            save_tasks(tasks)
            print(f"Task '{removed['task']}' deleted.")
        else:
            print("Invalid task number.")
    except ValueError:
        print("Please enter a valid number.")


def main():
    while True:
        tasks = load_tasks()
        print("\n" + "=" * 50)
        print("              TO-DO LIST")
        print("=" * 50)
        print("  1. View tasks")
        print("  2. Add task")
        print("  3. Complete task")
        print("  4. Delete task")
        print("  5. Exit")
        print("=" * 50)

        choice = input("\nChoose an option (1-5): ").strip()

        if choice == "1":
            view_tasks(tasks)
        elif choice == "2":
            add_task(tasks)
        elif choice == "3":
            complete_task(tasks)
        elif choice == "4":
            delete_task(tasks)
        elif choice == "5":
            print("Goodbye!")
            break
        else:
            print("Invalid option.")


if __name__ == "__main__":
    main()
