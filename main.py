# import the stuff needed
import random
import time
import riddles
import riddler

# ask the player what difficulty they want
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
else:
    random_element = random.randint(0, len(riddles.hard_riddle_questions)-1)
    y = riddles.hard_riddle_questions[random_element]
    z = riddles.hard_riddle_answers[random_element] 

users_riddle = riddler.Riddler(y,z)
print(y)
time.sleep(1)
# check if the answer is correct or wrong
a = 3
while (a < 6):
    b = input("Guess the answer to the riddle. You have" + a + "tries.")
    if (b != z):
        print("Ruh roh. You got it wrong, try again")
        a +=1
    else:
        print("Yay! You solved the riddle!")
        exit()