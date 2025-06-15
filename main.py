# import the stuff needed
import time
import riddler
import selection

# ask the player what difficulty they want
print("Please select difficulty level for your riddle.")
time.sleep(1)
choice =int(input( "\n 1: Easy \n 2: Medium \n 3: Hard \n "))


riddle = select_riddle(choice)
if riddle:
    question, answer = riddle
    game = Riddler(question, answer)
    game.ask()
else:
    print("Invalid choice. Exiting.")