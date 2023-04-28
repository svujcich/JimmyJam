import random
import time


# Correct yes or no choices
def validate_choice_yn(choice):
    while True:
        # choice = input("> ").upper().strip()
        if (choice == "Y") or (choice == "N"):
            return choice

        if (choice != "Y") or (choice != "N"):
            print("Try again with a valid selection! (Y / N)")
            choice = input("> ").upper().strip()

# correct ABCD choices
def validate_choice_abcd(choice):
    if (choice == "A") or (choice == "B") or (choice == "C") or (choice
                                                                 == "D"):
        return choice
    else:
        print("Try again with a valid selection! (Y / N)")
        choice = input("> ").upper().strip()

# Explain scenario ask if user wants to play
def intro_1():
    # INTRO
    print()
    print("Welcome to JIMMYJAM")
    print("------------------")
    print(
        "At a royal party, Jimmy accidentally spilled wine on the King and embarrassed him, so Jimmy’s punishment is death. Jimmy would like your help to persuade the King to let him off with a warning."
    )
    print()
    time.sleep(3)
    print("Are you willing to help Jimmy? (Y / N)")
    choice = input("> ").upper().strip()
    # funnel choice through function to catch incorrect entries
    choice = validate_choice_yn(choice)
    return choice


# Continue explaining scenario, ask for user name  
def intro_2():
    print()
    print("Great!")
    time.sleep(1)

    # capture username
    print("What can I call you?")
    username = input("> ").upper().strip()
    print()

    print(
        f"Oh, so you're {username}! Jimmy said you were best friends growing up. Great to meet you!"
    )
    print()
    time.sleep(3)
    print("Here's how you can help Jimmy...")
    print()
    time.sleep(1)

    print(
        "Earlier today, Jimmy came up with an argument he thinks might sway the King to spare him, but he forgot his argument!"
    )
    print()
    time.sleep(3)
    print(
        "Help Jimmy jog his memory to remember his key point before its too late!!"
    )
    print()
    time.sleep(2)
    return username
 

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
        
# Hangman - if guess is in keyword       
def letter_in_keyword(keyword, guess, correct_in_order, correct_guesses):
    for i, letter in enumerate(keyword):
        if letter == guess:
            correct_in_order[i] = f"{guess} "

            if letter not in correct_guesses:
                correct_guesses.append(letter)
    print("Correct!")
                          
def letter_not_in_keyword(guess, wrong_guesses, guess_count):
    if guess not in wrong_guesses:
        wrong_guesses.append(guess)
    print("Incorrect...")
    guess_count += 1
    return guess_count               

# print guessed letters and dashes on one line
def guess_progress(correct_in_order):
    print(correct_in_order[0], correct_in_order[1], correct_in_order[2], correct_in_order[3],\
    correct_in_order[4], correct_in_order[5], correct_in_order[6], correct_in_order[7],\
     correct_in_order[8], correct_in_order[9], correct_in_order[10], correct_in_order[11])


def display_gallows(guess_count):
    if guess_count == 0:
        print("---------")
        print("| /")
        print("|/")
        print("|")
        print("|")
        # print("_ " * len(keyword))

    elif guess_count == 1:
        print("---------")
        print("| /     O")
        print("|/")
        print("|")
        print("|")
        # print("_ " * len(keyword))

    elif guess_count == 2:
        print("---------")
        print("| /     O")
        print("|/      |")
        print("|")
        print("|")
        # print("_ " * len(keyword))

    elif guess_count == 3:
        print("---------")
        print("| /     O")
        print("|/      |\\")
        print("|")
        print("|")
        # print("_ " * len(keyword))

    elif guess_count == 4:
        print("---------")
        print("| /     O")
        print("|/     /|\\")
        print("|")
        print("|")
        # print("_ " * len(keyword))

    elif guess_count == 5:
        print("---------")
        print("| /     O")
        print("|/     /|\\")
        print("|        \\")
        print("|")
        # print("_ " * len(keyword))

    elif guess_count == 6:
        print("---------")
        print("| /     O")
        print("|/     /|\\")
        print("|      / \\")
        print("|")
        # print("_ " * len(keyword))

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


def validate_exit_game():
    print("Are you sure you want to exit? (Y / N)")
    choice = input("> ").upper().strip()
    choice = validate_choice_yn(choice)
    print()

    if choice == "Y":
        exit_game = True
    elif choice == "N":
        exit_game = False
    return exit_game

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
        exit_game = False
        correct_guesses = []
        wrong_guesses = []
        letter_choices = [
            "A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N",
            "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"
        ]
    
        # pick a random word for hangman
        keywords = [
            "AUTUMN", "PUMPERNICKEL", "DUSTBUNNY", "PICKELFORK", "SWIMSUIT"
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
            if (guess_count == 6) or ("_ " not in correct_in_order):
                break

            print()
            print("What would you like to do?")
            print("[A] Guess a letter")
            print("[B] Guess the word")
            print("[C] See incorrect guesses")
            print("[D] Exit Game")
            user_choice = input("> ").upper().strip()
    
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
    
            else:
                print("Try again with a valid selection")
                print()
    
        # User loses hangman - jump to end of script to see if player wants to play again
        if guess_count == 6:
            print("You Lose!")
            exit_game == False
        
        elif exit_game:
            break
        
        else:
            # CONTINUE
            time.sleep(1)
            print()
            print(f"OF COURSE!! The king loves {keyword}, he declared the second Tuesday of every month a holiday in honor of {keyword} after all!")
            print()
            time.sleep(3)
            print("Perhaps he will let Jimmy go if you can connect with him on a personal level and get creative with your approach...")
            print()
            time.sleep(2)
            print("Are you up for the challenge of persuading the King to let Jimmy go? (Y / N)")
            choice = input("> ").upper().strip()
            choice = validate_choice_yn(choice)
            if choice == "N":
                break
            print()
            
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
            
            # PERSUADE THE KING
            user_points = 3 # need 7 points to win
            
            print("You go to the castle")
            time.sleep(1)
            print("There is a long line of people waiting to see the King")
            time.sleep(1)
            print("What do you do?")
            time.sleep(1)
            print()
            print("[A] Stand at the back of the line")
            print("[B] Ask the gaurd to let you in")
            print("[C] Bypass the gaurd and kick the door open")
            print("[D] Exit game")
            choice = input("> ").upper().strip()
            validate_choice_abcd(choice)
            
            if choice == "A":
                print("You wait in line for 2 hours")
                
            elif choice == "B":
                print("You approach the gaurd")
                
            elif choice == "C":
                print("You bypass the gaurd and kick the door open")
                
        # If user loses, offer to continue playing   
        if exit_game == False:
            print("Do You Want to play Again?")
            choice = input("> ").upper().strip()
            
            if choice == "N":
                break
       

jimmyjam()


print()

print("GAME OVER")
        
        
        
        
    
    

               

        
    
    
    
    
    



