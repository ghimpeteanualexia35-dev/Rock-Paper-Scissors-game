import random

choices = ["piatra", "hartie", "foarfeca"]

def get_computer_choice():
    return random.choice(choices)

def determine_winner(user, computer):
    if user == computer:
        return "egal"

    if (
        (user == "piatra" and computer == "foarfeca") or
        (user == "foarfeca" and computer == "hartie") or
        (user == "hartie" and computer == "piatra")
    ):
        return "user"

    return "computer"
