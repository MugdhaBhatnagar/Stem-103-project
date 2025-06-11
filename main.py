# import the stuff needed
import random
import time

# Create a list of riddles
easyRiddleQuestions = ["What has an eye, but can not see?","What needs to be broken before it can be used?","What is full of holes but holds water?"]
easyRiddleAnswers = ["Needle","Egg","Sponge"]

mediumRiddleQuestions = ["What falls down but never breaks?"," I can fly without wings. I can cry without eyes. Wherever I go, darkness follows me. What am I?","What is easy to get into but hard to get out of?"]
mediumRiddleAnswers = ["Rain","Cloud","Trouble"]

hardRiddleQuestions = ["What always ends everything?","What is at the beginning of eternity, the end of time and space, the beginning of every end, and the end of every race?","Forwards I am heavy, backward I am not. What am I?"]
hardRiddleAnswers = ["G","E","Ton"]

# ask the player what difficulty they want
print("Please select difficulty level.")
time.sleep(2)
x = input( "1: Easy \n 2: Medium \n 3: Hard \n ")

# Create classes (maybe?)
class riddler:
    def __init__(difficulty, riddle, answer):
        self.difficulty = difficulty
        self.riddle = riddle
        self.answer = answer

# randomly generate a riddle from the difficulty level they chose
selectedDifficulty = int(x)
if (selectedDifficulty == 1):
    print("ok")
elif (selectedDifficulty == 2):
    print("mhm")
elif (selectedDifficulty == 3):
    print("oh well")
else:
    print("I ask the riddles, not you. Goodbye.")
    exit()


# check if the answer is correct or wrong
# if its correct, tell them they won
# if its wrong, give them 2 more chances