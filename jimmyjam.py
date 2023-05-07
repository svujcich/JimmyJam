import random
import time

# Correct choices with 2 options
def validate_choice_2(a, b):
    while True:
        choice = input("> ").upper().strip()
        if (choice == a) or (choice == b):
            return choice
        else:
            print(f"Try again with a valid selection! ({a} / {b})")
    

# Correct choices with 4 options
def validate_choice_4(a, b, c, d):
    while True:
        choice = input("> ").upper().strip()
        if (choice == a) or (choice == b) or (choice == c) or (choice == d):
            return choice
        else:
            print("Try again with a valid selection!")
 
 
def thinking():
    print()
    time.sleep(2)
    print(". . .")
    time.sleep(2)
    print()
           

# Explain scenario ask if user wants to play
def intro_1():
    # INTRO
    print()
    print("Welcome to JIMMYJAM")
    print("------------------")
    print("At a royal party, Jimmy accidentally spilled wine on the King and embarrassed him, so Jimmy’s punishment is death. Jimmy would like your help to persuade the King to let him off with a warning.")
    print()
    time.sleep(1)
    print("Are you willing to help Jimmy? (Y / N)")
    choice = validate_choice_2("Y", "N")
    return choice


# Continue explaining scenario, ask for user name  
def intro_2():
    print()
    print("Great!")
    time.sleep(1)
    print("What can I call you?")
    username = input("> ").upper().strip()
    print()
    print(f"Oh, so you're {username}! Jimmy said you were best friends growing up. Great to meet you!")
    print()
    time.sleep(2)
    print("Here's how you can help Jimmy...")
    print()
    time.sleep(1)
    print("Earlier today, Jimmy came up with an argument he thinks might sway the King to spare him, but he forgot his argument!")
    print()
    time.sleep(1)
    print("Help Jimmy jog his memory to remember his key point before its too late!!")
    print()
    time.sleep(1)
    return username
 

def display_gallows(guess_count):
    if guess_count == 0:
        print("---------")
        print("| /")
        print("|/")
        print("|")
        print("|")
        
    elif guess_count == 1:
        print("---------")
        print("| /     O")
        print("|/")
        print("|")
        print("|")        

    elif guess_count == 2:
        print("---------")
        print("| /     O")
        print("|/      |")
        print("|")
        print("|")      

    elif guess_count == 3:
        print("---------")
        print("| /     O")
        print("|/      |\\")
        print("|")
        print("|")
        

    elif guess_count == 4:
        print("---------")
        print("| /     O")
        print("|/     /|\\")
        print("|")
        print("|")     

    elif guess_count == 5:
        print("---------")
        print("| /     O")
        print("|/     /|\\")
        print("|        \\")
        print("|")
      
    elif guess_count == 6:
        print("---------")
        print("| /     O")
        print("|/     /|\\")
        print("|      / \\")
        print("|")
    
    
# Print guessed letters and dashes on one line
def guess_progress(correct_in_order):
    print(correct_in_order[0], correct_in_order[1], correct_in_order[2], correct_in_order[3],\
    correct_in_order[4], correct_in_order[5], correct_in_order[6], correct_in_order[7],\
     correct_in_order[8], correct_in_order[9], correct_in_order[10], correct_in_order[11])
  
  
# Validates hangman letter
def guess_again(guess, wrong_guesses, correct_guesses, letter_choices):
    while True:

        if len(guess) > 1:
            print("Too many characters, Try Again!")
            guess = input("> ").upper().strip()

        elif guess in wrong_guesses or guess in correct_guesses:
            print(f"you have already guessed {guess}. Try Again!")
            guess = input("> ").upper().strip()

        elif guess not in letter_choices:
            print("Not a valid entry, Try again!")
            guess = input("> ").upper().strip()

        else:
            return guess
    
        
# [A] Hangman - if letter is in keyword       
def letter_in_keyword(keyword, guess, correct_in_order, correct_guesses):
    for i, letter in enumerate(keyword):
        if letter == guess:
            correct_in_order[i] = f"{guess} "

            if letter not in correct_guesses:
                correct_guesses.append(letter)
    print("Correct!")
    
    
# [A] Hangman - if letter isn't in keyword                          
def letter_not_in_keyword(guess, wrong_guesses, guess_count):
    if guess not in wrong_guesses:
        wrong_guesses.append(guess)
    print("Incorrect...")
    guess_count += 1
    return guess_count     
     
          
# [C] Hangman - see incorrect guesses
def show_incorrect(wrong_guesses):
    if len(wrong_guesses) == 0:
        print("Wrong Guesses:[]")
        
    elif len(wrong_guesses) == 1:
        print(f"Wrong Guesses:[{wrong_guesses[0]}]")
        
    elif len(wrong_guesses) == 2:
        print(f"Wrong Guesses:[{wrong_guesses[0]}, {wrong_guesses[1]}]")
    
    elif len(wrong_guesses) == 3:
        print(f"Wrong Guesses:[{wrong_guesses[0]}, {wrong_guesses[1]}, {wrong_guesses[2]}]")
        
    elif len(wrong_guesses) == 4:
        print(f"Wrong Guesses:[{wrong_guesses[0]}, {wrong_guesses[1]}, {wrong_guesses[2]}, {wrong_guesses[3]}]")
        
    elif len(wrong_guesses) == 5:
        print(f"Wrong Guesses:[{wrong_guesses[0]}, {wrong_guesses[1]}, {wrong_guesses[2]}, {wrong_guesses[3]}, {wrong_guesses[4]}]")
        
    elif len(wrong_guesses) == 6:
        print(f"Wrong Guesses:[{wrong_guesses[0]}, {wrong_guesses[1]}, {wrong_guesses[2]}, {wrong_guesses[3]}, {wrong_guesses[4]}, {wrong_guesses[5]}]")


# Continue to castle 
# Check if user wants to continue playing after winning hangman
def continue_1(keyword):
    exit_game = False
    print()
    print(f"OF COURSE!! The king loves {keyword}, he declared the second Tuesday of every month a holiday in honor of {keyword} after all!")
    print()
    time.sleep(3)
    print("Perhaps he will let Jimmy go if you can connect with him on a personal level and get creative with your approach...")
    print()
    time.sleep(2)
    print("Are you up for the challenge of persuading the King to let Jimmy go? (Y / N)")
    choice = validate_choice_2("Y","N")
    print()
    if choice == "N":
        exit_game = True
    return exit_game


def continue_2(username):
    print("Great!")
    time.sleep(1)
    print("The castle is at the top of the hill, Jimmy is counting on you.")
    print()
    time.sleep(2)
    print(f"Good luck {username}!")
    print()
    time.sleep(1)
    print(". . . ")
    time.sleep(1)
    print()
    
    
def continue_3():
    print("You go to the castle")
    time.sleep(1)
    print("There is a long line of people waiting to see the King")
    print()
    time.sleep(1) 
 
 
# show adding and subtracting points 
def score(points, user_points):
    print(f"{points} points")
    print(f"Score: {user_points}")
  
  
def gaurd_menu(user_points):
    continue_3()
    print("What do you do?")
    time.sleep(1)
    print()
    print("[A] Stand at the back of the line")
    print("[B] Ask the gaurd to let you in")
    print("[C] Bypass the gaurd and kick the door open")
    print("[D] Exit game")
    print()
    print(f"Score: {user_points}")
    print("*** You need 7 points to win ***")
    choice = validate_choice_4("A", "B", "C", "D")
    return choice

       
def wait_in_line(user_points):
    user_points -= 2
    print()
    print("You wait in line for 2 hours")
    time.sleep(1)
    score("-2", user_points)
    thinking()
    time.sleep(1)
    print("You reach the front of the line")
    print()
    time.sleep(1)
    return user_points
 

def change_name(username,person):
    if person == "gaurd":
        print("GAURD: State your business.")
        print()
    elif person == "king":
        print("KING: Just who do you think you are?!")
        print()
    print("What do you do?")
    print("[A] Tell him your real name")
    print("[B] Give him an alias")
    new_name = validate_choice_2("A", "B")
    if new_name == "A":
        new_name = username
        return new_name
    else:
        print("What is your alias?")
        new_name = input("> ").upper().strip()
        return new_name
 
    
# demand gaurd introduces you to king
def introduction(a, b, new_name, user_points):
    gaurd_choice = random.randint(a, b)

    if gaurd_choice >= 1:
        # add 1 point if user is granted a royal introducation
        user_points += 1
        time.sleep(1)
        thinking()
        print("GAURD: Very Well")
        time.sleep(1)
        print("GAURD: From where did you travel?")
        hometown = input("> ").upper().strip()
        
        grand_entry = ["","*Corridor doors swing open*", "*Trumpets playing*",f"GAURD: Announcing {new_name} of {hometown}"]
        for line in grand_entry:
            print(line)
            time.sleep(1)
        score("+1", user_points)
        print()
        time.sleep(1)
        print("You enter the corridor . . . ")
        return user_points
            
    else:
        # add 0 points if a royal entrance is denied
        thinking()
        print("GAURD: Absolutely not, but the King will see you now.")
        time.sleep(1)
        print("*Corridor doors swing open*")
        time.sleep(1)
        print("you enter the corridor . . . ")
        score("+0", user_points)
        time.sleep(2)
        return user_points
                
# Choose: ask to see king / demand intro
def approach_gaurd(new_name, user_points,username):
    
    print()
    time.sleep(1)
    print("Then What?")
    time.sleep(1)
    print("[A] Tell the gaurd you are here to see the King")
    print("[B] Demand an introduction")
    business = validate_choice_2("A", "B") 
    
    if business == "B":
        
        business = "I demand a royal introduction to the King"

        print()
        print(f"{username}: I am {new_name} and {business}")

        noble_titles = ["KING", "QUEEN", "EMPEROR", "EMPRESS", "COUNT", "CPOUNTESS", "DUKE", "DUTCHESS", "PRINCE", "PRINCESS", "LORD", "LADY", "KNIGHT"]
        noble_name = False 
                        
        for noble in noble_titles:
            # if user name has noble title, 75% chance gaurd will announce user to the king
            if noble in new_name:
                noble_name = True
                
        if noble_name:
            user_points = introduction(0,3, new_name, user_points)
            return(user_points)
                
        # otherwise 50% chance gaurd will introduce    
        else:
            user_points = introduction(0,1, new_name, user_points)
            return(user_points)
        
    elif business == "A":
        business = "I am here to see the King. It's urgent!"
        # no points awarded
        print()
        print(f"{username}: I am {new_name} and {business}")
        thinking()
        print("GAURD: Very Well")
        time.sleep(1)
        print("*Corridor doors swing open*")
        time.sleep(1)
        print("You enter the corridor . . . ")
        time.sleep(2)
        score("+0", user_points)
        return(user_points)


# Greet the King
def bow_dramatically(user_points, new_name, username):
    user_points += 1
    print()
    print("*Bowing Dramatically on hands and knees*")
    time.sleep(1)
    print(f"{username}: My name is {new_name} his majesty")
    time.sleep(1)
    print("I am humbled to be in your presence")
    print()
    time.sleep(1)
    print("The King nods approvingly")
    score("+1", user_points) 
    return user_points
 
 
def quick_bow(user_points, new_name, username):
    user_points -= 1
    print()
    print("You preform a quick bow")
    time.sleep(1)
    print(f"{username}: His majesty, my name is {new_name}, thank you for seeing me. ")
    print()
    time.sleep(1)
    print("The King is unimpressed")
    score("-1", user_points)
    return user_points


def handshake(user_points, new_name, username):
    user_points -= 2
    print
    print("You approach the King and offer a handshake")
    print()
    time.sleep(1)
    print(f"{username}: Hello sir, I am {new_name}, charmed.")
    print()
    time.sleep(1)
    print("KING: How dare you!")
    time.sleep(1)
    print("The king slaps your hand away")
    score("-1", user_points)
    return user_points

     
# Talk with King - appologize/ compliment: print an appology, calculate user points
def chit_chat(strategy, position, keyword, user_points, username):

    # appology, points awarded, king response
    discussion_appology = [
        [f"{username}: As you may recall, a man named JIMMY spilled wine on you. Please accept my most humble appology on his behalf.", -2, "The King recalls how embarrased he was and scoffs"],
        [f"{username}: Your majesty, I cannot express how sorry I am about the wine incident, please have mercy.", 1, "The King feels compassion for the humble appology"],
        [f"{username}:The remorse in my heart for your soiled garbs is insufferanle, please spare the life of JIMMY.", -1, "The King appears annoyed at the repeated appologies"],
        [f"Your pain must feel as unbarable as having the joy of {keyword} removed from your heart",3, f"The King suddenly has an overwhelming sense of joy in thinking about {keyword}"]
    ]
    discussion_compliment = [        
        [f"{username}: Might I just say, what a gracious and merciful ruler you are, my lord. You radiate compassion, such that people of even the smallest of offenses, say, my friend JIMMY who spilled wine in your presence would repent for their actions. What a benevolent ruler you are!", 1, "The king wears your compliment with great pride"],
        [f"{username}: Might I also add how I admire the look of your crown atop your head. My friend JIMMY would agree, he has said many times how very becoming of you, my lord", 1, "The King feels especially good about himself"],
        [f"{username}: Your nose, his majesty, is as beautiful as the mountains", -2, "The King (who hates mountains) takes it as an insult"],
        [f"{username}: I meant not to offend you while commenting on your nose, what I meant was you wear it as majestically as this town wears its {keyword} holiday held the second Tuesday of every month!", 3, f"The King agrees his idea for a monthly {keyword} holiday is his greatest achievement as ruler to date!"]
    ]
    
    # decide which dictionary to use
    if strategy == "appology":
        discussion = discussion_appology
    elif strategy == "compliment":
        discussion = discussion_compliment
            
    # print conversation
    print()
    time.sleep(1)
    print(discussion[position][0])    
    print()
    time.sleep(1)
    print(discussion[position][2])
    time.sleep(1)
    
    # print score, calculate user_points
    # add a + symbol for score function if positive
    points = discussion[position][1]
    if points >= 1:
        user_points += points
        show_points = str(f"+{points}")
        score(show_points, user_points)
    else:
        user_points += points
        score(points, user_points)
    print()
    
    return user_points
 
 
def pitch_bluff(username):
    print()
    print(f"{username}: My lord . . .")
    time.sleep(1)
    print(f"{username}: Jimmy, the man who is about to hang is a SCIENTIST, and I am his Apprentice")
    time.sleep(1)
    print(f"{username}: The world is ending, there isn't much time")
    thinking()
       
# king only calls you Dr. if he believes your bluff      
def dr_username(new_name, username, points): 
    # check if username already has a DR. prefix
    for prefix in username:
        if username[0] + username[1] + username[2] == "DR.":
            prefix = True
        else:
            prefix = False
        
    if prefix == True:
        print()
        print(f"{username}Please his majesty, call me {new_name}")
        print()
        time.sleep(1)
        print("KING: Am I not already . . . ?")
        time.sleep(1)
        return new_name
    else:
        
        if points >= 1:
            if "DR." not in new_name:
                new_name = f"DR. {new_name}" 
            print()
            print(f"{username}: Please his majesty, call me {new_name}")
            print()
            time.sleep(1)
            print(f"KING: tell me more, {new_name}")
            print()
            time.sleep(1)
            return new_name
        
        else:
            print()
            print(f"{username}: Please his majesty, call me DR. {new_name}")
            print()
            time.sleep(1)
            print(f"KING: Absolutely not.")
            print()
            time.sleep(1) 
            return new_name
        
    
 
    
def gamble(bluff, user_points):
    king_reactions = {
    "surprised": ["KING: Are you serious?! How!","Wow! I thought for sure we had taken care of that last week when the stars were about to fall from the heavens"],
    "unconvinced": ["I don't believe you", "What kind of fool do you take me for?!"]
    }
    
    userpoints_fooledking = []
    
    # decide 1 point or 3 point at stake
    if bluff == 0:
        stakes = 1
    elif bluff == 1:
        stakes = 3
        
    # choose random number
    rand_bluff = random.randint(0,1)

    # If king believed you - print statement, calculate score, display score, return score
    if rand_bluff == 1:
        print(king_reactions["surprised"][bluff])
        print()
        time.sleep(1)
        
        user_points += stakes
        str_score = f"+{stakes}"
        score(str_score, user_points)
        time.sleep(1)            
        return stakes
    
    # If king thinks you're lying
    elif rand_bluff == 0:
        stakes = -stakes
        print(king_reactions["unconvinced"][bluff])
        print()
        time.sleep(1)
        
        user_points += stakes
        userpoints_fooledking.append(user_points)        
        
        score(stakes, user_points)
        time.sleep(1)            
        return stakes
    
    
def change_subject(username):
    print()
    print(f"{username}: Well you see I . . . ")
    time.sleep(1)
    print(f"*looks out the window*")
    time.sleep(1)
    print(f"{username}: Wow! was that a dragon?!")
    time.sleep(1)
    print (f"{username}: Those things just keep coming back don't they!")
    time.sleep(1)
    print(f"{username}: Anyways")
    time.sleep(1)
    print(f"{username}: What I was saying was . . . ")
    print()
    
    
def win_script(new_name):
    print()
    print("KING: I suppose I could let the wine fellow go this time")
    time.sleep(1)
    print(f"KING: But it better not happen again {new_name}!")
    time.sleep(1)
    print("KING: Gaurds! Release JIMMY")
    time.sleep(1)
    print() 
    print()
    print("----------------------------")
    print("CONGRATULATIONS!! YOU WON!!!")
    print("----------------------------")
    print()
 
 
def validate_exit_game():
    print("Are you sure you want to exit? (Y / N)")
    choice = validate_choice_2("Y", "N")
    print()

    if choice == "Y":
        exit_game = True
    elif choice == "N":
        exit_game = False
    return exit_game

def play_again():
    print("Do You Want to play Again? (Y / N)")
    choice = validate_choice_2("Y", "N")
    return choice


######################################


def jimmyjam():
    while True:
        # INTRO
        # explain scenario, ask if user wants to play
        accept_challenge = intro_1()
        if accept_challenge == "N":
            break
        
        # get username, continue explaining scenario 
        username = intro_2()
        
        # GAME SETUP
        guess_count = 0
        winner = False
        loser = False
        exit_game = False
        correct_guesses = []
        wrong_guesses = []
        letter_choices = [
            "A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N",
            "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"
        ]
    
        # pick a random word for hangman
        keywords = [
            "AUTUMN", "PUMPERNICKEL", "CONFETTI", "RUGBY", "AUSTRAILA",
            "YOGURT", "BOSTON", "GRANITE", "WOODWORKING", "TORTILLAS",
            "CANADA", "PORK", "GEOCACHING", "AMSTERDAM", "MOLD", "GOUDA",
            "UMPIRES", "LOGS", "HEADPHONES", "EDUCATION", "OHIO"
        ]
        selection = random.randint(0, len(keywords) - 1)
        keyword = keywords[selection]
    
        # create place holders for letters
        letter_1 = ""
        letter_2 = ""
        letter_3 = ""
        letter_4 = ""
        letter_5 = ""
        letter_6 = ""
        letter_7 = ""
        letter_8 = ""
        letter_9 = ""
        letter_10 = ""
        letter_11 = ""
        letter_12 = ""
    
        # store letters in list to access using loop
        correct_in_order = [
            letter_1,
            letter_2,
            letter_3,
            letter_4,
            letter_5,
            letter_6,
            letter_7,
            letter_8,
            letter_9,
            letter_10,
            letter_11,
            letter_12,
        ]
    
        # assign an _ for each letter in the keyword
        for i, letter in enumerate(keyword):
            correct_in_order[i] = "_ "
    
        # board setup
        display_gallows(guess_count)
        guess_progress(correct_in_order)
        # print(keyword)
    
        while True:
    
            # break loop if jimmy is completely on the board
            if (guess_count == 6):
                loser = True
                print()
                print(f"The word was {keyword}")
                print()
                break
            elif ("_ " not in correct_in_order):
                break

            print()
            print("What would you like to do?")
            print("[A] Guess a letter")
            print("[B] Guess the word")
            print("[C] See incorrect guesses")
            print("[D] Exit Game")
            user_choice = validate_choice_4("A", "B", "C", "D")
    
            if user_choice == "A":
                print("What letter do you guess?")
                guess = input("> ").upper().strip()
    
                while True:
                    # check if guess is valid
                    guess = guess_again(guess, wrong_guesses, correct_guesses,
                                        letter_choices)
    
                    if guess in keyword:
                        print()
                        letter_in_keyword(keyword, guess, correct_in_order, correct_guesses)
                        display_gallows(guess_count)
                        guess_progress(correct_in_order)
                        break
    
                    else:
                        print()
                        guess_count = letter_not_in_keyword(guess, wrong_guesses, guess_count)
                        display_gallows(guess_count)
                        guess_progress(correct_in_order)
                        break
    
                # print()
                
            # guess the word
            elif user_choice == "B":
                print("What do you think the word is?")
                word_guess = input("> ").upper().strip()
                
                if word_guess == keyword:
                    break
                else:
                    print()
                    print(f"Sorry, {word_guess} isn't correct")
                    guess_count += 1
                    display_gallows(guess_count)
                    guess_progress(correct_in_order)
                
            # see incorrect guesses
            elif user_choice == "C":
                show_incorrect(wrong_guesses)
                print()
    
            elif user_choice == "D":
                exit_game = validate_exit_game()

                if exit_game:
                    break

        # User loses hangman - jump to end of script to see if player wants to play again
        if guess_count == 6:
            loser = True
        
        elif exit_game:
            break
        
        else:
            # CONTINUE
            # Reveal keyword was guessed, ask player if they want to continue, if not break loop
            exit_game = continue_1(keyword)
            if exit_game:
                break
            continue_2(username)

            # PERSUADE THE KING
            user_points = 3 # need 7 points to win
            appology = 0
            bluff = 0
            compliment = 0
            
        
            print()
            # ARRIVE AT THE CASTLE
            choice = gaurd_menu(user_points)
            
            if choice == "A":
                # wait in line, lose 2 points
                user_points = wait_in_line(user_points)

                # reach front of line
                # ask if player wants to use an alias
                new_name = change_name(username, "gaurd")
                
                # talk to gaurd
                user_points = approach_gaurd(new_name, user_points, username)
                # print(user_points)
                print()
            
            if choice == "B":
                print()
                print("You skip to the front of the line")
                time.sleep(1)
                print()
                new_name = change_name(username, "gaurd")
                user_points = approach_gaurd(new_name, user_points, username)
                # print(user_points)
                print()
                                
            elif choice == "C":
                print()
                print("You bypass the gaurd and kick the door open")
                user_points -= 1
                time.sleep(1)
                score("-1", user_points)
                print()
                time.sleep(1)
                new_name = change_name(username, "king")
                print()
                
            elif choice == "D":
                exit_game = validate_exit_game()

                if exit_game:
                    break
                
            # GREET THE KING
            while True:
                if choice =="C":
                    print("Then What?")
                    time.sleep(1)
                else:
                    print("How do you greet the king?")
                    time.sleep(1) 
                print("[A] Bow dramatically on hand and knees") 
                print("[B] A quick bow as a formality") 
                print("[C] Go in for a handshake ")
                print("[D] Exit game")
                
                greeting = validate_choice_4("A", "B", "C", "D")

                if greeting == "A":
                    user_points = bow_dramatically(user_points, new_name, username)

                elif greeting == "B":
                    user_points = quick_bow(user_points, new_name, username)
                    
                elif greeting == "C":
                    user_points = handshake(user_points, new_name, username)
                    
                elif choice == "D":
                    exit_game = validate_exit_game()

                    if exit_game:
                        break
                    
                if user_points <=0:
                    loser = True
                    break
                
                # KING REACTS
                time.sleep(1)
                print()
                print("KING: State your business.")
                print()
                time.sleep(1)
                break
            
            while True: 
                            
                if user_points <= 0:
                    loser = True
                    break   
                
                if user_points >= 7:
                    winner = True
                    break 

                print("What do you do?")
                print("[A] Appologize")
                print("[B] Bluff")
                print("[C] Compliment")
                print("[D] Exit game")
                strategy = validate_choice_4("A", "B", "C", "D")
                
                if strategy == "A":
                    strategy = "appology"
                    user_points = chit_chat(strategy, appology, keyword, user_points, username)
                    appology += 1  
                    
                    if appology > 3:
                        appology = 0
                                        
                elif strategy == "B":
                    pitch_bluff(username)
                    points = gamble(bluff, user_points,)
                    user_points += int(points)
                    
                    bluff += 1
                    print()
                    time.sleep(1)

                    while True:
                         
                        if user_points >= 7:
                            winner = True
                            break
                        
                        if user_points <= 0:
                            loser = True
                            break
                        
                        print("What do you do?")
                        print("[A] insist the king addresses you as DR.")
                        print("[B] Change the subject")
                        print("[C] Double Down")
                        print("[D] Exit game")
                        choice = validate_choice_4("A", "B", "C", "D")
                        
                        if choice == "A":
                            new_name = dr_username(new_name, username, points)

                        elif choice == "B":
                            change_subject(username)
                            # reset bluff
                            bluff = 0
                            time.sleep(1)
                            break
                        
                        elif choice == "C":
                            print()
                            print(f"{username}: Only Jimmy knows how to synthesize aluminun bicarbonate to power the geo-magnitron!")
                            thinking()
                            points = gamble(bluff, user_points)
                            user_points += int(points)
                            if user_points <= 0:
                                loser = True
                            # reset bluff 
                            bluff = 0
                            break
                        
                        elif choice == "D":
                            exit_game = validate_exit_game()

                            if exit_game:
                                break
         
                elif strategy == "C":
                    strategy = "compliment"
                    user_points = chit_chat(strategy, compliment, keyword, user_points, username)
                    compliment += 1
                    
                    if compliment > 3:
                        compliment = 0
                             
                elif strategy == "D":
                    exit_game = validate_exit_game()
 
                if exit_game == True:
                    break
                        
        if exit_game == True:
            break
              
        # offer to continue playing
        if winner == True:
            win_script(new_name)
            choice = play_again()
            
            if choice == "N":
                break
        
        elif  loser == True and guess_count == 6:
            choice = play_again()
            if choice == "N":
                break
              
        elif loser == True:
            print()
            print("KING: I've had enough.")
            time.sleep(1)
            print(f"KING: Gaurds! take {new_name} away!")
            print()
            time.sleep(1)
            print("You Lose!")
            print()
            choice = play_again()
            
            if choice == "N":
                break
       

jimmyjam()

print()

print("GAME OVER")