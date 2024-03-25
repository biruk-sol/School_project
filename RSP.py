import random
def keepPlaying():
        while True:
            choice = input("Would like to keep playing? (Y or N) \n")
            choice = choice.capitalize()
            choices = ["Y", "N"]
            if choice in choices:
                break
            else:
                 print("Wrong choice! Try Again. \n")
        if choice == "Y":
            rspGame()
        else:
            print("Have a Good day! \n")
            
def rspGame():
    while True:
        print("Rock, Paper, Scissors Shoot: \n")
        player_Choice = input("Enter your choice: \t A.Rock B.Paper C.Scissors \n")
        player_Choice = player_Choice.capitalize()
        player_Choices = ["A", "B", "C"]
        if player_Choice in player_Choices:
            break
        else:
            print("Wrong choice! Try Again.")
    com_Choice = random.choice(player_Choices)
    if player_Choice == "A" and com_Choice == "A":
        print("Tie!")
        print("you choose: ", player_Choice, "and the computer choose: ", com_Choice, ". \n")
        keepPlaying()
    elif player_Choice == "A" and com_Choice == "B":
        print("Lost!")    
        print("you choose: ", player_Choice, "and the computer choose: ", com_Choice, ". \n")
        keepPlaying()
    elif player_Choice == "A" and com_Choice == "C":
        print("Won!")    
        print("you choose: ", player_Choice, "and the computer choose: ", com_Choice, ". \n")
        keepPlaying()
    elif player_Choice == "B" and com_Choice == "A":
        print("Won!")
        print("you choose: ", player_Choice, "and the computer choose: ", com_Choice, ". \n")    
        keepPlaying()
    elif player_Choice == ("B") and com_Choice == "B":
        print("Tie!")
        print("you choose: ", player_Choice, "and the computer choose: ", com_Choice, ". \n")    
        keepPlaying()
    elif player_Choice == ("B") and com_Choice == "C":
        print("Lost!")    
        print("you choose: ", player_Choice, "and the computer choose: ", com_Choice, ". \n")
        keepPlaying()
    elif player_Choice == ("C") and com_Choice == "A":
        print("Lost!")
        print("you choose: ", player_Choice, "and the computer choose: ", com_Choice, ". \n")    
        keepPlaying()
    elif player_Choice == ("C") and com_Choice == "B":
        print("Won!")
        print("you choose: ", player_Choice, "and the computer choose: ", com_Choice, ". \n")    
        keepPlaying()
    elif player_Choice == ("C") and com_Choice == "C":
        print("Tie!")
        print("you choose: ", player_Choice, "and the computer choose: ", com_Choice, ". \n")    
        keepPlaying()
