from datetime import date

habits = {}

def add_habit(name):
  if name not in habits:
    habits[name] = {"completed": []}
    print(f"Habit '{name}' added successfully!")
  else:
    print(f"Habit '{name}' already exists!")

def mark_complete(name):
  if name in habits:
    today = date.today()
    if today not in habits[name]["completed"]:
      habits[name]["completed"].append(today)
      print(f"Habit '{name}' marked completed for today!")
    else:
      print(f"Habit '{name}' already marked completed for today.")
  else:
    print(f"Habit '{name}' not found!")

def view_habits():
  if habits:
    for name, data in habits.items():
      completed_dates = ", ".join(str(d) for d in data["completed"])
      print(f"- {name} (Completed: {completed_dates})")
  else:
    print("No habits found.")

def habitTracker_main():
  while True:
    print("\nHabit Tracker")
    print("1. Add Habit")
    print("2. Mark Habit Complete")
    print("3. View Habits")
    print("4. Exit")

    choice = input("Enter your choice: ")

    if choice == '1':
      name = input("Enter habit name: ")
      add_habit(name)
    elif choice == '2':
      name = input("Enter habit name to mark complete: ")
      mark_complete(name)
    elif choice == '3':
      view_habits()
    elif choice == '4':
      print("Exiting...")
      break
    else:
      print("Invalid choice. Please try again.")

if __name__ == "__main__":
  habitTracker_main()
