def escape_room():
    """ (str) -> Nonetype
    Takes an imput as a string and prints out a string. This function is an escape room that has a list of commands where each command gives a
    clue until you enter in the special command, "Meghan", in which the game will end. If not, the game will keep going until the command is
    entered.
    >>> eXaMine the floating Cd
    The contact you make with the golded cd called "Watch the Throne" causes it to play the Paris song...but it only plays a loop of one lyric:
    "Prince Willia_s ain't do it right, if you ask me Cause I was him, I would have married Kate and Ashl_y."
    Remember, every prince has a princess.
    >>> LEAVE
    Invalid Command
    >>> Meghan
    YOU HAVE ESCAPED THE ROYAL FAMILY JUST LIKE MEGHAN MARKLE!!!! CONGRATS!     
"""
    print("You have been hypnotized by the Royal Guards of England for treason and now find yourself in an endless loop. Suddenly, "
          "you hear the voice of the six God, Aubrey Graham A.K.A the Champagne Papi, A.K.A the \"Sticky\" artist, A.KA the Drizzy Drakey Poo."
          " In awe, you call out his name, but he silences you, stating:\n"
          "\"Drake might quite possibly be the type of guy to be stuck in a trance,\nBut thy is also the type to give you a chance.\n"
          "So here are some clues to guide you to freedom,\nFind the key word to escape this, GO READER!\""
          " \nA Drake teleports you to a room with a floating cd, "
          "a Basqiuat panting, and a Portrait of Dido Elizabeth Belle.")
    
    
    commands = "examine the floating cd\nexamine the Basquiat painting\nexamine the Portrait of Dido Elizabeth Belle"
    What_will_you_do = ""
    while True:
        What_will_you_do = input("What will you do? ")
        if What_will_you_do.lower() == "list commands":
            print(commands)
        elif "cd" in What_will_you_do.lower():
            print("The contact you make with the golded cd called \"Watch the Throne\" causes it to play the Paris song..."
                  "but it only plays a loop of one lyric: \"Prince Willia_s ain't do it right, if you ask me "
                  "Cause I was him, I would have married Kate and Ashl_y.\" Remember, every prince has a princess.")
        elif "basquiat" in What_will_you_do.lower(): 
            print("You look at the description: Basquiat, an artist with Haitian heritage, famous for the infamous crowns in his paintin_s."
            "One mig_t say that he is royalty.")
        elif "elizabeth" in What_will_you_do.lower():
            print("You look at the description: Dido Eliz_beth Belle, the daughter of a British _aval officer, is known as the first black"
                  " aristocrat. Which other British royal had black origins?")
        elif What_will_you_do.lower() == "meghan":
            print("YOU HAVE ESCAPED THE ROYAL FAMILY JUST LIKE MEGHAN MARKLE!!!! CONGRATS!")
            break
        else:   
            print("Invalid Command")