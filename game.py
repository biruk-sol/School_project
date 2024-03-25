def gameMainMenu():
    while True:
        game_choice = input("\n What game would like to play: ")
        print("1, Rock, Paper, Scissors")
        print("2, Hang Man")
        print("3, Number guessing")
        import RSP
        import hangMan
        import numberGuessing
        if game_choice == "1":
            RSP.rspGame()
            break
        elif game_choice == "2":
            hangMan.playerGuess()
            break
        elif game_choice == "3":
            numberGuessing.guessnumber()
            break
        else:
            print("ERROR! Try again")
            continue
