# project number four 

import random

def get_computer_choice():
    choices = ["rock", "paper", "scissors"]
    return random.choice(choices)

def determine_winner(user, computer):

    if user == computer:
        return "It's a tie!"

    elif user == "rock" and computer == "scissors":
        return "You win!"

    elif user == "paper" and computer == "rock":
        return "You win!"

    elif user == "scissors" and computer == "paper":
        return "You win!"

    else:
        return "Computer wins!"


print("🎮 Welcome to Rock Paper Scissors")

user_choice = input("Choose rock, paper, or scissors: ").lower()

computer_choice = get_computer_choice()

print(f"Computer chose: {computer_choice}")

result = determine_winner(user_choice, computer_choice)

print(result)





