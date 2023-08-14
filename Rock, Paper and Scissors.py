# User and  the computer
# rules for the simple
# Rock smashes Scissors
# Paper covers Rock
# Scissor will cut the Paper

import random

user=input("Enter a command (Rock, Paper ,and Scissors")
list_1=["Rock","Paper","Scissors"]
computer=random.choice(list_1)
print("You chose", user)
print("The computer chose", computer)

if user== computer:
    print(" It's a tie")
elif user=="Rock":
    if computer=="Paper":
        print("computer wins")
    else:
        print("user wins")
elif user=="Paper":
    if computer=="Rock":
        print("user wins")
    else:
        print("computer wins")
elif user=="Scissors":
    if computer=="Paper":
        print("user wins")
    else:
        print("computer wins")
else:
    print("Not valid input")