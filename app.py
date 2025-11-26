tasks = []

def add_task(task):
    """Add a new task to the list."""
    if not task.strip():
        print("Task cannot be empty.")
        return
    tasks.append(task)
    print(f"Added: {task}")

def list_tasks():
    """Display all tasks."""
    if not tasks:
        print("No tasks.")
        return
    print("\n--- Tasks ---")
    for i, task in enumerate(tasks, 1):
        print(f"{i}. {task}")

def delete_task(index_str):
    """Delete a task by its number."""
    try:
        idx = int(index_str.strip()) - 1
        if 0 <= idx < len(tasks):
            removed = tasks.pop(idx)
            print(f"Removed: {removed}")
        else:
            print("Invalid task number.")
    except ValueError:
        print("Enter a valid task number.")

def main():
    print("=== Simple CLI To-Do List ===\n")

    while True:
        print("Commands: [add/list/delete/exit]")
        user_input = input("> ").strip()

        if user_input.lower() == "exit":
            print("Goodbye!")
            break
        elif user_input.lower() == "list":
            list_tasks()
        elif user_input.lower().startswith("add "):
            add_task(user_input[4:])
        elif user_input.lower().startswith("delete "):
            delete_task(user_input[7:])
        else:
            print("Unknown command.\n")

if __name__ == "__main__":
    main()
