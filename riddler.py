import time
import riddles
import random

def initialize_game():
    print("Hello! Welcome to the Riddle Game! \nYou have to select a riddle difficulty and try to answer the riddle within 3 tries.")
    time.sleep(1)

def select_riddle(difficulty):
    
    if(difficulty == 1):
        random_element = random.randint(0, len(riddles.easy_riddle_questions)-1)
        y = riddles.easy_riddle_questions[random_element]
        z = riddles.easy_riddle_answers[random_element]
    elif (difficulty == 2):
        random_element = random.randint(0, len(riddles.medium_riddle_questions)-1)
        y = riddles.medium_riddle_questions[random_element]
        z = riddles.medium_riddle_answers[random_element]
    elif (difficulty == 3):
        random_element = random.randint(0, len(riddles.hard_riddle_questions)-1)
        y = riddles.hard_riddle_questions[random_element]
        z = riddles.hard_riddle_answers[random_element]
    else:
        print("I ask the riddles, not you. Goodbye.")
        exit()
    return y,z

def ask(ridd,answer):
    time.sleep(1)
    print(ridd)
    time.sleep(1)
    attempt = 3
    for attempts in range(3,6):
        user_input = input(f"Enter your answer. You have {attempt} attempts remaining ")
        if (user_input == answer):
            print("Yay! you solved the riddle!")
            play_more()

        else:
            print("No, that's not it...")
            attempt = attempts - 1

    print(f"You're out of luck. The correct answer was: {answer}")

def play_more():
    continue_playing = input("Do you want to continue playing? Type Y for yes or N for no. ")
    if (continue_playing == 'Y'):
        difficulty = int(input("Select riddle difficulty. Enter 1 for easy, 2 for medium, or 3 for hard. "))
        ridd,answer = select_riddle(difficulty)
        ask(ridd,answer)
        return continue_playing,difficulty,ridd,answer
    else:
        print("Goodbye.")
