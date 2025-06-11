# import the stuff needed
import random
import time

# Create a list of riddles
easy_riddle_questions = ["What has an eye, but can not see?","What needs to be broken before it can be used?","What is full of holes but holds water?"]
easy_riddle_answers = [" Needle"," Egg"," Sponge"]

medium_riddle_questions = ["What falls down but never breaks?"," I can fly without wings. I can cry without eyes. Wherever I go, darkness follows me. What am I?","What is easy to get into but hard to get out of?"]
medium_riddle_answers = ["Rain","Cloud","Trouble"]

hard_riddle_questions = ["What always ends everything?","What is at the beginning of eternity, the end of time and space, the beginning of every end, and the end of every race?","Forwards I am heavy, backward I am not. What am I?"]
hard_riddle_answers = ["G","E","Ton"]

# ask the player what difficulty they want
print("Please select difficulty level.")
time.sleep(2)
x = input( "\n 1: Easy \n 2: Medium \n 3: Hard \n ")

# Create classes (maybe?)
class Riddler:
    def __init__(difficulty, riddle, answer):
        self.difficulty = difficulty
        self.riddle = riddle
        self.answer = answer

# randomly generate a riddle from the difficulty level they chose
selectedDifficulty = int(x)
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


# check if the answer is correct or wrong
# if its correct, tell them they won
# if its wrong, give them 2 more chances