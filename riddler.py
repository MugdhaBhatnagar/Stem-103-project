import time

class Riddler:
    def __init__(self,riddle, answer, max_attempts = 3):
        self.riddle = riddle
        self.answer = answer
        self.max_attempts = max_attempts

def ask(self):
    print(self.riddle)
    time.sleep(1)
    for attempt in range(1, self.attempt + 1):
        user_input = input(f"Enter your answer. You have {attempt}/{self.max_attempts}: remaining")
        if (user_input == self.answer):
            print("Yay! you solved the riddle!")
            return True
        else:
            print("No, that's not it...")
    print(f"You're out of luck. The correct answer was: {self.answer}")
    return False