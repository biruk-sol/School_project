import To_do
import habit_tracker
import game

def mainmenu():
    while True:
        print("\t WELCOME TO THE STUDENT PORTAL!")
        print("1, To do list ")
        print("2, Habit tracker")
        print("3, Games")
        user_choice = input("What do you like to do: ")
        if user_choice == "1":
            To_do.todo_main()
            break
        elif user_choice == "2":
            habit_tracker.habitTracker_main()
            break
        elif user_choice == "3":
            game.gameMainMenu()
            break
        else:
            print("ERROR! Try again")
            continue

mainmenu()