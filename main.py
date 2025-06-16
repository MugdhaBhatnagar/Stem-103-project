# import functions from riddler
from riddler import *

# initialize the game
initialize_game()

# Get the user's difficulty preferance
time.sleep(1)
difficulty = int(input("Select riddle difficulty. Enter 1 for easy, 2 for medium, or 3 for hard. "))

# Store the riddle and the correct answer
ridd,answer = select_riddle(difficulty)

# Ask the riddle, ask if user wants to continue playing
ask(ridd,answer)


