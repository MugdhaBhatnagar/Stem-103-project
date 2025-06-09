# create CSV file for the riddles
# import the stuff needed
import csv
import random

output_file = 'riddles.csv'
# ask the player what difficulty they want

# randomly generate a riddle from the difficulty level they chose
# take input from the user
# check if the answer is correct or wrong
# if its correct, tell them they won
# if its wrong, give them 2 more chances


# Create classes (maybe?)
class riddler:
    def __init__(difficulty, riddle, answer):
        self.difficulty = difficulty
        self.riddle = riddle
        self.answer = answer

print(''' _  _  _____  __  __    ___  _____  __  _  _  ____  ____     ____  _  
( \/ )(  _  )(  )(  )  / __)(  _  )(  )( \/ )( ___)(  _ \   (_  _)( )_( )( ___)
 \  /  )(_)(  )(__)(   \__ \ )(_)(  )(__\  /  )__)  )(_) )    )(   ) _ (  )__) 
 (__) (_____)(______)  (___/(_____)(____)\/  (____)(____/    (__) (_) (_)(____)
____  ____  ____  ____  __    ____    /\                                       
(  _ \(_  _)(  _ \(  _ \(  )  ( ___)  )(                                       
 )   / _)(_  )(_) ))(_) ))(__  )__)                                          
(_)\_)(____)(____/(____/(____)(____)  ()                                       ''')