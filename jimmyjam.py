import random
import time


# yes or no
def validate_choice(choice):
    while True:
        # choice = input("> ").upper().strip()
        if (choice == "Y") or (choice == "N"):
            return choice

        if (choice != "Y") or (choice != "N"):
            print("Try again with a valid selection! (Y / N)")
            choice = input("> ").upper().strip()


# assign an _ for each letter in the keyword
def reassign_letters(keyword, correct_letters):
    i = 0

    num_letters = len(keyword)
    while i < num_letters:
        correct_letters[i] = "_ "
        i += 1
        break


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
        print("_ " * len(keyword))

    elif guess_count == 1:
        print("---------")
        print("| /     O")
        print("|/")
        print("|")
        print("|")
        print("_ " * len(keyword))

    elif guess_count == 2:
        print("---------")
        print("| /     O")
        print("|/      |")
        print("|")
        print("|")
        print("_ " * len(keyword))

    elif guess_count == 3:
        print("---------")
        print("| /     O")
        print("|/      |\\")
        print("|")
        print("|")
        print("_ " * len(keyword))

    elif guess_count == 4:
        print("---------")
        print("| /     O")
        print("|/     /|\\")
        print("|")
        print("|")
        print("_ " * len(keyword))

    elif guess_count == 5:
        print("---------")
        print("| /     O")
        print("|/     /|\\")
        print("|        \\")
        print("|")
        print("_ " * len(keyword))

    elif guess_count == 6:
        print("---------")
        print("| /     O")
        print("|/     /|\\")
        print("|      / \\")
        print("|")
        print("_ " * len(keyword))


def add_letters(guess):
    if guess in keyword:
        for i, letter in enumerate(keyword):
            if letter == guess:

                if letter not in correct_guesses:
                    correct_guesses.append(letter)
                    return (i, letter)
    else:
        print(f"{guess} is NOT in {keyword}")
        wrong_guesses.append(guess)

        answer = add_letters(guess)


# test = ["this", "that"]

# print(test[0] + test[1])

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
        choice = validate_choice(choice)

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
        # prints hangman board
        display_gallows(wrong_guesses, keyword)

        # assigns an _ for each letter in the KEYWORD
        reassign_letters(keyword, correct_in_order)

        # shows letters that have been guessed correctly in the KEYWORD
        # guess_progress(correct_in_order)

        while True:
            print()
            print("What would you like to do?")
            print("[A] Guess a letter")
            print("[B] Guess the word")
            print("[C] See incorrect guesses")
            print("[D] Exit Game")
            user_choice = input("> ").upper().strip()

            if user_choice == "A":
                print("You chose A")
                print()

            elif user_choice == "B":
                print("You chose B")
                print()

            elif user_choice == "C":
                print("You chose C")
                print()

            elif user_choice == "D":
                print("Are you sure you want to exit? (Y / N)")
                choice = input("> ").upper().strip()
                choice = validate_choice(choice)
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

print("GAME OVER")

        
        
        
        
    
    

               

        
    
    
    
    
    



