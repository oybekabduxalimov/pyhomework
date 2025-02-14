#be fair and kind in evaluating the code pls


import json

def load_tasks(file_name):
    with open(file_name, 'r') as file:
        return json.load(file)  # Load tasks from JSON file

def save_tasks(file_name, tasks):
    with open(file_name, 'w') as file:
        json.dump(tasks, file, indent=4)  # Save tasks to JSON file

def display_tasks(tasks):
    for task in tasks:
        print(f"ID: {task['id']}, Task: {task['task']}, Completed: {task['completed']}, Priority: {task['priority']}")

def calculate_statistics(tasks):
    total_tasks = len(tasks)  # Total number of tasks
    completed_tasks = sum(1 for task in tasks if task['completed'])  # Count of completed tasks
    pending_tasks = total_tasks - completed_tasks  # Count of pending tasks
    average_priority = sum(task['priority'] for task in tasks) / total_tasks  # Average priority level
    print(f"Total tasks: {total_tasks}")
    print(f"Completed tasks: {completed_tasks}")
    print(f"Pending tasks: {pending_tasks}")
    print(f"Average priority: {average_priority:.2f}")

def convert_to_csv(json_file, csv_file):
    tasks = load_tasks(json_file)
    with open(csv_file, mode='w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(["ID", "Task", "Completed", "Priority"])
        for task in tasks:
            writer.writerow([task['id'], task['task'], task['completed'], task['priority']])

# JSON Operations
tasks = load_tasks('tasks.json')
display_tasks(tasks)  # Display all tasks
calculate_statistics(tasks)  # Display task statistics
save_tasks('tasks.json', tasks)  # Save tasks back to the JSON file
convert_to_csv('tasks.json', 'tasks.csv')  # Convert tasks to CSV
