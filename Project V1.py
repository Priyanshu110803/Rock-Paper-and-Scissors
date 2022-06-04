# Project 1 V.1
# Rock,Paper and Scissors
# Testing the Basic mechanisms of Game

import random

player_choice = input("Choose one out of Rock , Paper and Scissors : ")
print(player_choice)
computer_choices = ["Rock","Paper","Scissors"]
choice_taken = random.choice(computer_choices)
print(choice_taken)
if player_choice == choice_taken :
    print("Selected The Same")
else:
    print("beep...beep")
      