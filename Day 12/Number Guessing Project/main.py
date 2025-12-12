import random
from art import logo

EASY_LEVEL_TURNS=10
HARD_LEVEL_TURNS=5

def set_difficulty():
    difficulty = input("Choose a difficulty level 'easy' or 'hard': ' ").lower()
    if difficulty == "easy":
        return EASY_LEVEL_TURNS
    else:
        return HARD_LEVEL_TURNS

def check_guess(actual_number, guess,turns):
    if guess > actual_number:
        print("Too high.")
        return turns- 1
    elif guess < actual_number:
        print("Too low.")
        return turns-1
    else:
        print(f"you have guessed the right number {actual_number}.")


def game():
    print(logo)
    print("Welcome to the Number Guessing Game!")
    print("I'm thinking of a number between 1 and 100.")

    actual_number = random.randint(1,100)
    print(f"psst the number is {actual_number}.")
    turns = set_difficulty()
    guess = 0
    while guess != actual_number:
        print(f"you have {turns} turns left to guess the right number.")
        guess = int(input("make a guess: "))
        turns = check_guess(actual_number, guess, turns)
        if turns == 0:
            print("you have used all your guesses.you lose.")
            return
        elif guess != actual_number:
            print("guess again")

game()
