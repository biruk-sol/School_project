import random
def guessnumber():
    while True: 
        domain = []
        domain.extend(range(10))
        chosen_Number = random.choice(domain)
        print("Welcome to the 'guess the number' game")
        guess = int(input("Guess a number from 1 to 10: \n"))
        trial = 5
        while guess != chosen_Number:
            trial -= 1
            print("Wrong guess! you have ", trial, " chances left.")
            guess = int(input("Try again \n"))
            if trial == 1:
                break
        break
    if guess == chosen_Number:
        print("You have won! The number was: ", chosen_Number, ".\n")
    else:
        print("Game over. The number was: ", chosen_Number)
    while True:
        keepPlaying = input("Would you like to keep playing? (Y OR N) \n")
        keepPlaying = keepPlaying.capitalize()
        if keepPlaying == "Y" or keepPlaying == "N":
            break
        else:
            print("Wrong choice! Try Again")
    if keepPlaying == "Y":
        guessnumber()
    else: 
        print("Have a nice day!")    


