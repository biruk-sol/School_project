def load_tasks():
  tasks = []
  try:
    with open("tasks.txt", "r") as f:
      for line in f:
        task, completed = line.strip().split(",")
        tasks.append({"task": task, "completed": completed == "True"})
  except FileNotFoundError:
    pass  
  return tasks

def save_tasks(tasks):
 
  with open("tasks.txt", "w") as f:
    for task in tasks:
      f.write(f"{task['task']},{task['completed']}\n")

def view_tasks(tasks):
 
  if tasks:
    for i, task in enumerate(tasks, start=1):
      status = "Completed" if task["completed"] else "Pending"
      print(f"{i}. {task['task']} ({status})")
  else:
    print("No tasks found!")

def add_task(tasks):
  task = input("Enter task description: ")
  tasks.append({"task": task, "completed": False})
  print(f"Task '{task}' added successfully!")

def mark_task(tasks):
  if tasks:
    view_tasks(tasks)
    index = int(input("Enter task number to mark (or 0 to cancel): "))
    if 0 < index <= len(tasks):
      tasks[index - 1]["completed"] = not tasks[index - 1]["completed"]
      status = "Completed" if tasks[index - 1]["completed"] else "Pending"
      print(f"Task '{tasks[index - 1]['task']}' marked {status}.")
    else:
      print("Invalid task number!")
  else:
    print("No tasks to mark!")

def delete_task(tasks):
  if tasks:
    view_tasks(tasks)
    index = int(input("Enter task number to delete (or 0 to cancel): "))
    if 0 < index <= len(tasks):
      deleted_task = tasks.pop(index - 1)
      print(f"Task '{deleted_task['task']}' deleted successfully.")
    else:
      print("Invalid task number!")
  else:
    print("No tasks to delete!")

def todo_main():
  tasks = load_tasks()

  while True:
    print("\nTo-Do List")
    print("1. View Tasks")
    print("2. Add Task")
    print("3. Mark Task Complete/Pending")
    print("4. Delete Task")
    print("5. Save and Exit")

    choice = input("Enter your choice: ")

    if choice == '1':
      view_tasks(tasks)
    elif choice == '2':
      add_task(tasks)
    elif choice == '3':
      mark_task(tasks)
    elif choice == '4':
      delete_task(tasks)
    elif choice == '5':
      save_tasks(tasks)
      print("Tasks saved and exiting...")
      break
    else:
      print("Invalid choice. Please try again.")

if __name__ == "__main__":
  todo_main()
