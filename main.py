# import the stuff needed
# ask the player what difficulty they want
import random
# randomly generate a riddle from the difficulty level they chose
# Create classes (maybe?)
class riddler:
    def __init__(difficulty, riddle, answer):
        self.difficulty = difficulty
        self.riddle = riddle
        self.answer = answer
# take input from the user
x = input("Please select difficulty level. \n 1: Easy \n 2: Medium \n 3: Hard ")
print(x)
# check if the answer is correct or wrong
# if its correct, tell them they won
# if its wrong, give them 2 more chances