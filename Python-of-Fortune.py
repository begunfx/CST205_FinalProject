###### Team 4 Final Project ######
#      William Gillihan          #
#      Christopher Dixon         #
#      Wendy Gray                #
#      Brian Begun               #
#                                #
#      ver 12.07.15              #
#      12_07_2015                #
##################################


#Start the game function
def pythonOfFortune():

  #Player starting dollar amount initialized
  playerDollars = 1000
  
  #Welcome Screen
  printNow("\n|======================|")
  printNow("Welcome to the PYTHON OF FORTUNE!")
  printNow("\n")
  
  printNow("Before playing the game you must load the")
  printNow("sound file.")
  
  #Because we cannot set relative path in this itteration of JES
  #we have to ask the player to load the game sound file
  dialogFile = pickAFile()
  dialogClip = makeSound(dialogFile)
  userMenu(dialogClip)
  
#Player Menu
#You can type exit at any time to leave the game.  
def userMenu(dialogClip):
  
  #Game menu options
  printNow("\n---GAME MENU---\n")
  printNow("Type one of the following options:\n")
  printNow("spin - spin the wheel and guess a letter")
  printNow("play sound - play the completed part of the puzzle")
  printNow("exit - type at anytime to quit the game.")

  #While loop to keep player in the game until they choose to leave
  stillPlaying = true
  choice = None
  while stillPlaying:
    choice = requestString("Make your selection: ")
    if choice == None:
      printNow("\nThat's not an option, please try again.")
      stillPlaying = true
    elif choice == "":
      printNow("\nYou didn't enter anything, please try again.")
      stillPlaying = true
    else:
      choice = choice.lower()
      if choice == "exit":
        printNow("\nYour quitting?  You suck!  Goodbye.")
        stillPlaying = false
        return
      elif choice == "spin":
        #spinResult = spinWheel()
        newGuess = true
        while newGuess == true:
          guessLetter = requestString("Please guess a letter")
          if guessLetter == None:
            printNow("\nThat's not an option, please try again.")
            newGuess == true
          elif guessLetter == "":
            printNow("\nYou didn't enter anything, please try again.")
            newGuess = true
          else:
            guessLetter = guessLetter.lower()
            if guessLetter == "exit":
              printNow("\nYou're giving up all that money?  Okay.  See ya.")
              newGuess = false
              return
            if len(guessLetter) > 1:
              printNow("\nOne character only, please try again.")
              newGuess = true
            elif guessLetter.isnumeric():
              printNow("\nNumbers are not allowed, please try again.")
              newGuess = true
      else:
        printNow("\nThat's not an option, please try again.")
        stillPlaying = true      