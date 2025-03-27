from utils.validation import validation
from random import randint

import numpy as np
import pandas as pd

arr = np.array([1, 2, 3, 4])
sri = pd.Series([5, 6, 8, 5])

def start_game():
    random_number = randint(1, 100)
    while True:
        input_number = input("Please inter your guess number: ")
        
        if input_number == "q":
            print("Thank you for playing game, Good bye")
            break
        if not validation(input_number):
            continue
        
        input_number = int(input_number)
        if (input_number > 100) or (input_number < 1):
            print("Please inter te number between 1 and 100: ")
            continue
        
        if input_number == random_number:
            print(f"Good for you for guessing{random_number}")
            break
        elif input_number < random_number:
            print("Your guess is low")
            continue
        else:
            print("Your guess is high")
            continue
        
if __name__ == "__main__":
    start_game()

    