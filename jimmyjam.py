import random
import time


# yes or no
def validate_choice_yn(choice):
    while True:
        # choice = input("> ").upper().strip()
        if (choice == "Y") or (choice == "N"):
            return choice

        if (choice != "Y") or (choice != "N"):
            print("Try again with a valid selection! (Y / N)")
            choice = input("> ").upper().strip()
            
def calidate_choice_abcd(choice):
    if (choice == "A") or (choice == "B") or (choice == "C") or (choice == "D"):
        return choice
    else:
        print("Try again with a valid selection! (Y / N)")
        choice = input("> ").upper().strip()
        
def guess_again(guess, wrong_guesses, correct_guesses):        
    if guess in wrong_guesses or guess in correct_guesses:
        print(f"you have already guessed {guess}. Try Again!")
        guess = input("> ")
        return guess


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


def guess_progress(correct_in_order):
    print(correct_in_order[0], correct_in_order[1], correct_in_order[2], correct_in_order[3],\
    correct_in_order[4], correct_in_order[5], correct_in_order[6], correct_in_order[7],\
     correct_in_order[8], correct_in_order[9], correct_in_order[10], correct_in_order[11])
    # print(keyword)


def display_gallows(wrong_guesses, keyword):
    guess_count = len(wrong_guesses)
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
        
        
# guess = "K"
# keyword = "ALPHABEAT"
# correct_guesses = ["B"]
# wrong_guesses = ["X", "M"]

# def add_letters(guess, keyword, correct_guesses, wrong_guesses):
#     # position = []
#     if guess in keyword:
#         for i, letter in enumerate(keyword):
#             if letter == guess:
#                 # print(i, letter)
#                 correct_in_order[i] = f"{guess} "
                
#                 if letter not in correct_guesses:
#                     correct_guesses.append(letter)
                    
#     else:
#         print(f"{guess} is NOT in {keyword}")
#         if guess not in wrong_guesses:
#             wrong_guesses.append(guess)


# verdict = add_letters(guess, keyword, correct_guesses, wrong_guesses)
# print(verdict)
# print(correct_guesses)
# print(wrong_guesses)




#------------------


def jimmyjam():
    while True:
        # INTRO
        print()
        print("Welcome to JIMMYJAM")
        print("------------------")
        print(
            "At a royal party, Jimmy accidentally spilled wine on the King and embarrassed him, so Jimmy’s punishment is death. Jimmy would like your help to persuade the King to let him off with a warning."
        )
        print()
        time.sleep(4)
        print("Are you willing to help Jimmy? (Y / N)")
        choice = input("> ").upper().strip()
        # funnel choice through function to catch incorrect entries
        choice = validate_choice_yn(choice)

        if choice == "N":
            break

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
            "Earlier today, Jimmy came up with an argument he thinks might sway the King to spare him, but he forgot."
        )
        print()
        time.sleep(3)
        print(
            "Help Jimmy jog his memory to remember his key point before its too late!!"
        )
        print()
        time.sleep(2)

        # GAME SETUP
        correct_guesses = []
        wrong_guesses = []
        letter_choices = ["A", "B", "C", "D", "E", "F", "G","H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]

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
        display_gallows(wrong_guesses, keyword)
        guess_progress(correct_in_order)
        # print(keyword)

        while True:
            # break loop if jimmy is completely on the board
            if len(wrong_guesses) == 6:
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
                    # check i letter is in key word

                    if len(guess) > 1:
                        print(f"Too many characters, Try Again!")
                        guess = input("> ").upper().strip
                        
                    elif guess not in letter_choices:
                        print("Not a valid entry, Try again!")
                        guess = input("> ").upper().strip
                                     
                    elif guess in wrong_guesses or guess in correct_guesses:
                        print(f"you have already guessed {guess}. Try Again!")
                        guess = input("> ")
                                                                      
                    elif guess in keyword:
                        print()

                        for i, letter in enumerate(keyword):
                            if letter == guess:
                                # print(i, letter)
                                correct_in_order[i] = f"{guess} "
                                
                                if letter not in correct_guesses:
                                    correct_guesses.append(letter)
                        print("Correct!")                    
                        display_gallows(wrong_guesses, keyword)
                        guess_progress(correct_in_order)
                        break   
                                    
                    else:
                        print()
                        if guess not in wrong_guesses:
                            wrong_guesses.append(guess)
                        print("Incorrect...")
                        display_gallows(wrong_guesses, keyword)
                        guess_progress(correct_in_order)
                        break
                                        
                # print()

            elif user_choice == "B":
                print("You chose B")
                print()

            elif user_choice == "C":
                print("You chose C")
                print()

            elif user_choice == "D":
                print("Are you sure you want to exit? (Y / N)")
                choice = input("> ").upper().strip()
                choice = validate_choice_yn(choice)
                print()

                # ends game - second while loop
                if choice == "Y":
                    break

            else:
                print("Try again with a valid selection")
                print()

        # end game - first while loop
        break


jimmyjam()

print()
print("GAME OVER")

        
        
        
        
    
    

               

        
    
    
    
    
    



