import sys
import os

TODO_FILE = "todo.txt"

def load_tasks():
    tasks = []
    if os.path.exists(TODO_FILE):
        with open(TODO_FILE, 'r') as file:
            tasks = [line.strip() for line in file.readlines()]
    return tasks

def save_tasks(tasks):
    with open(TODO_FILE, 'w') as file:
        for task in tasks:
            file.write(task + '\n')

def add_task(task):
    tasks = load_tasks()
    tasks.append(task)
    save_tasks(tasks)
    print(f'Added task: "{task}"')
    view_tasks()

def view_tasks():
    tasks = load_tasks()
    if not tasks:
        print("No tasks found.")
    else:
        for i, task in enumerate(tasks, 1):
            print(f'{i}. {task}')

def complete_task(task_number):
    tasks = load_tasks()
    if 0 < task_number <= len(tasks):
        task = tasks.pop(task_number - 1)
        save_tasks(tasks)
        print(f'Completed task: "{task}"')
    else:
        print("Invalid task number.")
    view_tasks()

def delete_task(task_number):
    tasks = load_tasks()
    if 0 < task_number <= len(tasks):
        task = tasks.pop(task_number - 1)
        save_tasks(tasks)
        print(f'Deleted task: "{task}"')
    else:
        print("Invalid task number.")
    view_tasks()

def print_help():
    help_text = """
    Usage:
      todo.py add [task]            Add a new task
      todo.py view                  View all tasks
      todo.py complete [task_num]   Mark a task as completed
      todo.py delete [task_num]     Delete a task
      todo.py help                  Show this help message
    """
    print(help_text)

def main():
    if len(sys.argv) < 2:
        print_help()
        return

    command = sys.argv[1]

    if command == "add":
        if len(sys.argv) < 3:
            print("Please provide a task to add.")
        else:
            task = ' '.join(sys.argv[2:])
            add_task(task)
    elif command == "view":
        view_tasks()
    elif command == "complete":
        if len(sys.argv) < 3:
            print("Please provide a task number to complete.")
        else:
            try:
                task_number = int(sys.argv[2])
                complete_task(task_number)
            except ValueError:
                print("Task number should be an integer.")
    elif command == "delete":
        if len(sys.argv) < 3:
            print("Please provide a task number to delete.")
        else:
            try:
                task_number = int(sys.argv[2])
                delete_task(task_number)
            except ValueError:
                print("Task number should be an integer.")
    else:
        print_help()

if __name__ == "__main__":
    main()
