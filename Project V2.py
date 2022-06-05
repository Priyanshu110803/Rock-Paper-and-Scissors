# Project 1 V.1
# Rock,Paper and Scissors
# Testing the Basic mechanisms of Game

import random
rounds_left = int(input("Enter the Number of Round you Want to Play : "))

player_choice = input("Choose one out of Rock , Paper and Scissors : ")
print(player_choice)
computer_choices = ["Rock","Paper","Scissors"]
choice_taken = random.choice(computer_choices)
print(choice_taken)

if player_choice == choice_taken :
    print("Selected The Same")
    
elif player_choice == "Paper" and choice_taken == "Rock" or player_choice == "Scissors" and choice_taken == "Paper" or player_choice == "Rock" and choice_taken == "Scissors":
    print ('Player Won this Round ')
    print ('Number of Rounds Left : ' , rounds_left -1)
    
elif player_choice == "Rock" and choice_taken == "Paper" or player_choice == "Paper" and choice_taken == "Scissors" or player_choice == "Scissors" and choice_taken == "Rock":
    print ('Computer Won this Round ')
    print ('Number of Rounds Left : ' , rounds_left - 1)
