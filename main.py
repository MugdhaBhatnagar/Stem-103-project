# import the stuff needed
import random
import time
import riddles

# ask the player what difficulty they want
a = 0
while (a < 3):
    print("Please select difficulty level.")
    time.sleep(2)
    x = input( "\n 1: Easy \n 2: Medium \n 3: Hard \n ")
    if (x == 1):
        y = random.choice(riddles.easy_riddle_questions)
        z = riddles.easy_riddle_answers(y)
    print(y)
elif:
# check if the answer is correct or wrong
# if its correct, tell them they won
# if its wrong, give them 2 more chances
if (selectedDifficulty == 1):
    random_element = random.randint(0, len(easy_riddle_questions)-1)
    easy_riddle = easy_riddle_questions[random_element]
    easy_answer = easy_riddle_answers[random_element]

#  The print statement is there for me to see if the code is working
    print(easy_riddle + easy_answer)

# Remove the riddle so it doesn't get repeated
    easy_riddle_questions.remove(random_element)
    easy_riddle_answers.remove(random_element)

elif (selectedDifficulty == 2):
    random_element = random.randint(0, len(easy_riddle_questions)-1)
    easy_riddle = easy_riddle_questions[random_element]
    easy_answer = easy_riddle_answers[random_element]
else:
    print("I ask the riddles, not you. Goodbye.")
    exit()