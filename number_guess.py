import random

EASY_LEVEL_TURNS = 10
HARD_LEVEL_TURNS = 5

def compare(user_guess, actual_answer, turns):
    if user_guess > actual_answer:
        print("Too high.")
        return turns - 1
    elif user_guess < actual_answer:
        print("Too low.")
        return turns - 1
    else:
        print(f"You got it! The answer was {actual_answer}")

def set_difficulty():
    level = input("Choose a difficulty - 'easy or 'hard': ")
    if level == "easy":
        return EASY_LEVEL_TURNS
    else:
        return HARD_LEVEL_TURNS

def play_game():
    print("Welcome - Number guessing game")
    print("I am thinking of a number between 1 and 100")
    answer = random.randint(1, 100)

    turns = set_difficulty()

    guess = 0
    while guess != answer:
        print(f"You have {turns} attempts remaining")
        guess = int(input("Make a guess: "))
        turns = compare(guess, answer, turns)
        if turns == 0:
            print("You've run out of guesses, you lose.")
            print(f"The correct answer was {answer}")
            return
        elif guess != answer:
            print("Guess again.")
play_game()
