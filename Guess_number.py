import random
import os
os.system("cls")

def guess_number():
    print("Welcome to the Guess the Number game!")
    print("I'm thinking of a number between 1 and 100.")
    secret_number = random.randint(1, 100)
    attempts = 0
    
    while True:
        guess = int(input("Take a guess: "))
        attempts += 1
        
        if guess < secret_number:
            print("Too low! Try again.")
        elif guess > secret_number:
            print("Too high! Try again.")
        else:
            print("Congratulations! You guessed the number in", attempts, "attempts.")
            break

guess_number()
