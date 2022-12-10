import random
import os
from art import logo
# Scree clearing function
def cls():
    os.system('cls' if os.name=='nt' else 'clear')

# Random number from 1 to 100
number_selected = random.randint(1, 100)

# function to assign number of attempts depending on difficulty chosen
def difficulty(level):
    if level == "hard":
        return 5
    elif level == "easy":
        return 10

# Function to start the game
def play_game():
    # Welcome screen and play choice
    print(logo)
    print("\n")
    print("Welcome to Cosby Number Guessing Game 🤔")
    print("I'm thinking of a number from 1 to 100")
    level_choice = input("Choose a difficulty level to start the game, type 'hard' or 'easy': ").lower()
    attempts = difficulty(level_choice)
    print("\n")

    # Game over condition
    is_game_over = False
    # While loop to allow multiple guessing
    while attempts > 0 and not is_game_over:
        print(f"You have {attempts} attempts remaining to guess the number!")
        # User guess
        guess = int(input("Make a guess: "))
        # After guess message and penalization/action
        if guess > number_selected:
            attempts -= 1
            print("Too high")
        elif guess < number_selected:
            attempts -= 1
            print("Too low")
        elif guess == number_selected:
            is_game_over = True
            print(f"You guessed right, the number is {number_selected}. You win🤗")
        if attempts == 0:
            print("You are out of attempts, you lose😓")

    # Repeat game choice
    print("\n")
    play_again = input("Do you want to play again? Type 'y' for yes, 'n' for no: ").lower()
    if play_again == "y":
        cls()
        play_game()

play_game()
