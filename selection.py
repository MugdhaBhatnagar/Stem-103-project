import random
import riddles

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