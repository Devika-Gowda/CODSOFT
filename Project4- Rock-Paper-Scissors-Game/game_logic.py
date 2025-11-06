import random

choices = ["rock", "paper", "scissors"]
score = {"user": 0, "computer": 0}
target_score = 0

def set_target(target):
    global target_score
    target_score = target
    score["user"] = 0
    score["computer"] = 0

def get_computer_choice():
    return random.choice(choices)

def determine_winner(user_choice, computer_choice):
    if user_choice == computer_choice:
        return "tie"
    elif (user_choice == "rock" and computer_choice == "scissors") or \
         (user_choice == "paper" and computer_choice == "rock") or \
         (user_choice == "scissors" and computer_choice == "paper"):
        score["user"] += 1
        return "user"
    else:
        score["computer"] += 1
        return "computer"

def get_score():
    return score

def check_final_winner():
    if target_score == 0:
        return None
    if score["user"] >= target_score:
        return "User"
    elif score["computer"] >= target_score:
        return "Computer"
    else:
        return None

def reset_game():
    global target_score
    target_score = 0
    score["user"] = 0
    score["computer"] = 0
