import time
import riddles
import random

#  Sends the welcome statement and tells the player about the rules of the game
def initialize_game():
    print("Hello! Welcome to the Riddle Game! ")
    time.sleep(1)
    print("You have to select a riddle difficulty and try to answer the riddle within 3 tries.")
    time.sleep(1)

# Selects a random riddle and its correct answer from the difficulty the player chose
def select_riddle(difficulty):
    if(difficulty == 1):
        random_element = random.randint(0, len(riddles.easy_riddle_questions)-1)
        ridd = riddles.easy_riddle_questions[random_element]
        answer = riddles.easy_riddle_answers[random_element]
    elif (difficulty == 2):
        random_element = random.randint(0, len(riddles.medium_riddle_questions)-1)
        ridd = riddles.medium_riddle_questions[random_element]
        answer = riddles.medium_riddle_answers[random_element]
    elif (difficulty == 3):
        random_element = random.randint(0, len(riddles.hard_riddle_questions)-1)
        ridd = riddles.hard_riddle_questions[random_element]
        answer = riddles.hard_riddle_answers[random_element]
    else:
        print("I ask the riddles, not you. Goodbye.")
        exit()
    return ridd,answer

# Takes input from the player and checks to see if its correct
def ask(ridd,answer):
    time.sleep(1)
    print(ridd)
    time.sleep(1)
    for attempts in range(3,0,-1):
        user_input = input(f"Enter your answer. You have {attempts} attempts remaining ")
        if (user_input == answer):
            print("Yay! you solved the riddle!")
            play_more()

        else:
            print("No, that's not it...")

    print(f"You're out of luck. The correct answer was: {answer}")
    play_more()

# Asks the player if they want to play this game again. Repeats if they do.
def play_more():
    continue_playing = input("Do you want to continue playing? Type Y for yes or N for no. ")
    if (continue_playing == 'Y'):
        difficulty = int(input("Select riddle difficulty. Enter 1 for easy, 2 for medium, or 3 for hard. "))
        ridd,answer = select_riddle(difficulty)
        ask(ridd,answer)
        return continue_playing,difficulty,ridd,answer
    else:
        print("Goodbye.")
        exit()
