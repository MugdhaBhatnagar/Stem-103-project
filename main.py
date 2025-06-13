# import the stuff needed
import random
import time
import riddles
import riddler

# ask the player what difficulty they want
a = 0
while (a < 3):
    print("Please select difficulty level for your riddle.")
    time.sleep(1)
    x = input( "\n 1: Easy \n 2: Medium \n 3: Hard \n ")
    if(x == 1):
        random_element = random.randint(0, len(riddles.easy_riddle_questions)-1)
        y = riddles.easy_riddle_questions[random_element]
        z = riddles.easy_riddle_answers[random_element]
    elif (x == 2):
        random_element = random.randint(0, len(riddles.medium_riddle_questions)-1)
        y = riddles.medium_riddle_questions[random_element]
        z = riddles.medium_riddle_answers[random_element]
    elif (x == 3):
        random_element = random.randint(0, len(riddles.hard_riddle_questions)-1)
        y = riddles.hard_riddle_questions[random_element]
        z = riddles.hard_riddle_answers[random_element] 
    else:
        print("I ask the riddles, not you. Goodbye.")
        exit()
    users_riddle = riddler.Riddler(x,y,z)
    print(y)
    time.sleep(1)
    b = input("Guess the answer to the riddle. You have 3 tries.")
# check if the answer is correct or wrong
# if its correct, tell them they won
# if its wrong, give them 2 more chances