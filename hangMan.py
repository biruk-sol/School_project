from words import word_list
import random
def display_hangman(tries):
    stages = [  # final state: head, torso, both arms, and both legs
                """
                   --------
                   |      |
                   |      O
                   |     \\|/
                   |      |
                   |     / \\
                   -
                """,
                # head, torso, both arms, and one leg
                """
                   --------
                   |      |
                   |      O
                   |     \\|/
                   |      |
                   |     / 
                   -
                """,
                # head, torso, and both arms
                """
                   --------
                   |      |
                   |      O
                   |     \\|/
                   |      |
                   |      
                   -
                """,
                # head, torso, and one arm
                """
                   --------
                   |      |
                   |      O
                   |     \\|
                   |      |
                   |     
                   -
                """,
                # head and torso
                """
                   --------
                   |      |
                   |      O
                   |      |
                   |      |
                   |     
                   -
                """,
                # head
                """
                   --------
                   |      |
                   |      O
                   |    
                   |      
                   |     
                   -
                """,
                # initial empty state
                """
                   --------
                   |      |
                   |      
                   |    
                   |      
                   |     
                   -
                """
    ]
    return stages[tries]
def word():
    choosen_word = random.choice(word_list).upper()
    return choosen_word
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
            playerGuess()
        else:
            print("Have a Good day! \n")
def playerGuess():
    tries = 6
    choosen_word = word()
    guess_word = []
    complete_word = "_" * len(choosen_word)
    print("Let's play Hangman! Guess the word: ", complete_word)
    while guess_word != choosen_word and tries > 0:
        print(display_hangman(tries))
        guess_letter = input("Guess the a letter: \n").upper()
        if guess_letter.isalpha() and len(guess_letter) == 1 :
         if guess_letter in guess_word:
               print("ERROR! You have already guessed this one. Try again.")
               continue
         elif guess_letter not in choosen_word:
             print("The letter ", guess_letter, " is not in the word.")
             tries = tries - 1
             guess_word.append(guess_letter)
         elif guess_letter in choosen_word:
               print("Good job,", guess_letter, " is in the word!")
               guess_word.append(guess_letter)
               indices = [i for i, letter in enumerate(choosen_word) if letter == guess_letter ]
               for index in indices:
                     word_as_list = list(complete_word)
                     word_as_list[index] = guess_letter
                     complete_word = "".join(word_as_list)
               print(complete_word)
               if "_" not in complete_word:
                   break
        else: 
            print("Error: enter again!")
    if complete_word != choosen_word:
      print(display_hangman(tries))
      print("Sorry, you ran out of tries. The word was " + choosen_word + ". Maybe next time!")
    else: 
        print("Congrats, you guessed the word! You win! \n")
    keepPlaying()

