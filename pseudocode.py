# print PROJECT NAME
# ------------------
# NARRATOR gives intro
'''
At a royal party, Jimmy accidentally spilled wine on the King and embarrassed him, so Jimmy’s punishment is death. Jimmy needs our help to find the right word to persuade the king to let him off with a warning. 
'''
# prompt user to enter name
# save player name

# NARRATOR recalls how player knows Jimmy
# NARRATOR asks player to indicate if they are ready to help Jimmy
# prompt user to select Y or N
    # loop until valid selection is entered



# ---HANGMAN----
# NARRRATOR explains objective of hangman
'''
Jimmy has argument he thinks might sway the King, but he caht remember te KEYWORD. Help Jimmy remember the KEYWORD before it is too late!
'''
# program selects a KEYWORD from a list of words
# program prints out board 
# program prints ouf a blank space for each letter
# -----------  
# |  /
# |/
# |
# |
#   _ _ _ _ _ 

# loop

    # create list for letter guesses

    # prompt user
        # guess the word OR
        # select a letter OR 
        # view letter guesses OR
        # exit game

    # if user chooses select a letter
        # prompt user to enter guess 
        # save letter guessed

        # if letter is in KEYWORD
            # CORRECT - adds letter to blank space
            # adds letter to letter guess list

        # if letter is NOT in KEYWORD
            # print letter NOT in KEYWORD
            # print a the next body part in the sequence
            # add letter to letter guesses list

    # if user chooses guess the KEYWORD
        # prompt user to enter guess

        # if user KEYWORD guess is CORRECT
            # break loop

        # if user guess is NOT KEYWORD
            # print wrong guess
            # add next body part in sequence

    # if user chooses view letter guesses
        # print letters already guessed

    #  if user selects exit    
        # program asks if they are sure (Y / N)

    # if all of Jimmy's body parts are on the board
        # break loop GAME OVER
     # --------
    # |  /    O
    # |/     /|\
    # |     _/ \_
    # |
    #   A _ _ R _ R N 
        
    # program loops until     
        # correct KEYWORD is guessed OR
        # every letter in KEYWORD filled in OR
        # Jimmy runs out of time, GAME OVER.

# loop breaks
    
# if GAME OVER
    # tell player they lose
    #  ask if they want to play again
        # if yes, reset the game with new KEYWORD
        # if no quit the game.

# otherwise, game CONTINUES


# -----VISIT THE KING-----
# NARRATOR explains how the KEYWORD might be able to sway the king
# storyline continues
# user goes to the castle

# user_points = 3
# user gains and loses user points based on King's reaction
# need 7 points to persuade the king to release jimmy
# points always on back end. 
# if user_points = 0, GAMEOVER

# User STRATEGIES
    # APPOLOGIZE - beg for mercy
    # BLUFF- claim you are a scientist
    # COMPLIMENT - charm the king 

# asks do you want to choose and alias?
    # prompts user to enter new USERNAME
    # if user name contains noble sirname (ex. LADY, LORD) +1 
    # if entered, the KING will call you by your alias until the end of the conversation
    
# prompt the user to make an entrance
    # stand in line to see the KING -2
    # ask the gaurd to let you in
        # option to demand an introduction +1
    # bypass the guards and kick the door open -1

# prints KING recation
    
# prompt user is aksed to select an introduction
    # bowing dramatically on hand and knees +1
    # a quick bow as a formality
    # go in for a handshake -1

# print KING reaction
# KING asks state your business
# prompts user to select from MAIN MENU 

# loop
    # MAIN MENU
    # if APPOLOGIZE
        # keep track of the hunber of times APPOLOGIZE is chosen
        # appologize = 0
        # after all APPOLOGIZE options chosen, starts over with first option when appologize selected
    
        # if appologize = 0
            # user explain the true story 
            # KING remembers how embarrased he was -2
            # (appologize = appologize +1)
            # back to MAIN MENU
    
        # if appologize = 1
            # show humility +1
            # KING feels compassion
            # (appologize = appologize +1)
            # back to MAIN MENU

        # if appologize = 2
            # show humility, different words
            # KING is annoyed -1
            # (appologize = appologize +1)
            # back to MAIN MENU
    
        # if appologize = 3
            # show humility, use KEYWORD +3
            # KING feels compassion
            # (appologize = 0)
            # back to MAIN MENU
        
        
    # if BLUFF
        # user claims Jimmy ia an SCIENTIST, and user is Jimmy's Apprentice
        # the world is ending, there isn't much time +1
    
        # KING asks user to explain
        # user explains the sun is about to fall out of the sky
        # Only a master SCIENTIST can transform metal into air to hold sun in place
        
        # KING thinks - program waits for KING to think
            # 50/50 shot that he believes you
    
            # if KING believes user
                # user points = user points + 1
    
            # if KING does NOT believe USER
                # user points = user points - 1
    
            # KING makes a remark

            # BLUFF MENU
            # prompts user to make a selection
                # ALIAS - tell the king to call you DR. username
                    # KING calls user DR. username until conversation ends +1
                    # can only be selected once
                    # loops back to BLUFF MENU
    
                # CHANGE SUBJECT - go back to MAIN MENU
    
                # DOUBLE DOWN - Continue to make up story
                    # Only Jimmy knows how to synthesize aluminun bicarbonate 
                    # to power the geo-magnitron
    
                    # KING thinks - program waits for KING to think
                     # 50/50 shot that he believes you
    
                        # if KING believes user
                            # user points = user points + 3
                
                        # if KING does NOT believe USER
                            # user points = user points - 3
    
                    # Back to MAIN MENU
    
    # if COMPLIMENT 
        # keep track of the hunber of times COMPLIMENT is chosen
        # compliment = 0
        # after all COMPLIMENT options chosen, starts over with first option when COMPLIMENT selected
    
        # if compliment = 0
            # worship KING, tell him how awesome and merciful is 
            # KING reacts positively +1
            # (compliment = compliment + 1)
            # back to MAIN MENU
    
        # if compliment = 1
            # compliment his crowm, very becomming of him
            # KING agrees his crown fits him +1
            # (compliment = compliment + 1)
            # back to MAIN MENU
    
        # if compliment = 2
            # compliment his nose
            # KING takes it as an insult -2
            # (compliment = compliment + 1)
            # back to MAIN MENU
    
        # if compliment = 3
            # explain last compliment was meant to flatter him
            # incorporate KEYWORD +3
            # KING is flattered

    # if EXIT game selected
        # asks user if they are sure they want to exit the game (Y / N)
        # if YES
            # print GAME OVER
            # loop breaks     
        # in NO 
            # back to MAIN MENU
    
# if user points >= 7 loop breaks
# KING agrees to release Jimmy
# user WINS GAME

# if user points <= 0 loop breaks
# KING kicks user out of the castle
# user loses GAME OVER

# ask user if they want to play again (Y / N)
    # if YES - restart game
    # if NO - game ends