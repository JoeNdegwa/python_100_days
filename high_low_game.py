"""
Display Art
Generate a random account from data
Format the account data into printable format
Ask user for a guess
Check if user is correct
Get follower count of each account
Use if statement to check is user is correct
Give user feedback on their guess
Keep score
Make the game repeatable
Make account at position B become the next account at position A
"""
from game_data import data
from art import logo, vs
import random


# Format the account data into printable format
def format_account(text, account):
    account_name = account["name"]
    account_description = account["description"]
    account_country = account["country"]
    return f"{text}: {account_name}, a {account_description} from {account_country}"


def check_answer(guess, account_a_followers, account_b_followers):
    if account_a_followers > account_b_followers:
        return guess == "a"
    else:
        return guess == "b"


# Display Art
print(logo)
score = 0
account_b = random.choice(data)
continue_game = True
while continue_game:
    # Generate a random account from data
    account_a = account_b
    account_b = random.choice(data)
    if account_a == account_b:
        account_b = random.choice(data)

    print(format_account("Compare A", account_a))
    print(vs)
    print(format_account("Against B", account_b))
    # Ask user for a guess
    guess = input("Who has more followers? Type 'A' or 'B': ").lower()
    # Check if user is correct
    # Get follower count of each account
    account_a_follower = account_a["follower_count"]
    account_b_follower = account_b["follower_count"]
    is_correct = check_answer(guess, account_a_follower, account_b_follower)
    # Use if statement to check is user is correct
    # Give user feedback on their guess
    if is_correct:
        score += 1
        print(f"You are right! Current Score is: {score}")
    else:
        print(f"Sorry that's wrong. Final Score: {score}")
        continue_game = False
