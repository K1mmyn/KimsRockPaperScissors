
import random
from simple_colors import *
import math

user_wins = 0
computer_wins = 0
game_complete = 3

def user_won():
    print(green("\nUser Won! ", 'bold'))

def rps_commands():
    print("\n (1) Rock \n (2) Paper \n (3) Scissors \n (123) Quit")

def user_vs_bot_score():
    print(f"Your Score was: {user_wins} vs the computer score of: {computer_wins} \n\nDo you want to play again?\n(Y)es or (N)o\n")

def ty_play():
    print(cyan("\nThank you for playing Kim's Rock Paper Scissors\n", 'bold'))

def printScore():
    print(f"\nUser score: {user_wins}")
    print(f"Computer score: {computer_wins}")

def user_won():
    print(green("\nUser Won! ", 'bold'))
    printScore()

def bot_won():
    print(red("\nComputer Won! ", 'bold'))
    printScore()

def getinputint(msg):
    while True:
        try:
            return int(input(msg))
        except:
            print("\nPlease Enter a valid command...")
            continue

print(green("\nWelcome to Kim's Rock Paper Scissors", 'bold'))
rps_commands()      

while True:
    choice = getinputint("\n> ")
    bot_choice = int(random.randint(1,3))
    if choice == 123:
        ty_play()
        quit()
    if choice == bot_choice:
            print(magenta("\nIt's a Tie", 'bold'))
            printScore()
            continue
    elif (choice == 1):
        if (bot_choice == 3):
            user_wins += 1
            user_won()
        else:            
            computer_wins += 1
            bot_won()
    elif (choice == 2):
        if (bot_choice == 1):
            user_wins += 1
            user_won()
        else:
            computer_wins += 1
            bot_won()
    elif (choice == 3):
        if (bot_choice == 2):
            user_wins += 1
            user_won()
        else:
            computer_wins += 1
            bot_won()
    elif (choice == 123):
        ty_play()
        quit()

    if user_wins == game_complete:
        while True:
            print(green("\nYou Won! \n", 'bold'))
            user_vs_bot_score()
            again = input("> ").lower()
            match again:
                case "y":
                    user_wins = 0
                    computer_wins = 0
                    rps_commands()
                    break
                case "n":
                    ty_play()
                    quit()
                case _:
                    continue
                
    if computer_wins == game_complete:
        while True:
            print(red("\nYou Lost! 🥲\n", 'bold'))
            user_vs_bot_score()
            again = input("> ").lower()      
            match again:
                case "y":
                    user_wins = 0
                    computer_wins = 0
                    rps_commands()
                    break
                case "n":
                    ty_play()
                    quit()
                case _:
                    continue
            



