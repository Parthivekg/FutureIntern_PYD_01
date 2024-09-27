import random

lower_range = 1
upper_range = 100
answer = random.randint(lower_range,upper_range)
guesses = 0
playing = True
print("Welcome to Number Guessing Game")
print(f"select a number between {lower_range} and {upper_range}")

while playing:

    guess = int(input("Enter your guess:"))
    if guess<lower_range or guess>upper_range:
        print("Invalid guess")
        print(f"Please select a number between {lower_range} and {upper_range}")

    elif guess<answer:
        print("Too less! Try again") 
        guesses+=1
    elif guess>answer:
        print("Too high! Try again")
        guesses+=1
    else:
        print("You Guessed Correct answer")
        print(f"Number of guesses:{guesses}")
        playing = False


                


