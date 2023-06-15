# Python Game Task

import random
# user and CPU
# Welcome message

print("Welcome to the dice game, Are you ready to play?")  # welcome message
print("Can user win please enter your name? ")
user_wins = input()  # to
import random # it imports a random generated number
user_wins = 0 #initial score is 0 for both user and cpu
CPU_wins = 0

while True:
    user_wins_dice1 = random.randint(1, 6)  # using random.randint to roll the dice between 1 and 6
    user_wins_dice2 = random.randint(1, 6)
    user_wins = user_wins_dice1 + user_wins_dice2  # adding values between both dice

    CPU_wins_dice1 = random.randint(1, 6)
    CPU_wins_dice2 = random.randint(1, 6)
    CPU_wins = CPU_wins_dice1 + CPU_wins_dice2

    if user_wins > CPU_wins: # using if statement to compare the values
        print("YOU WIN!!!")
        user_wins += 1  # so when user wins they get a point

    elif user_wins == CPU_wins:
        print("It's a Tie")
    else:
        print("CPU WINS!!!!")
        CPU_wins += 1


    print(f"\nyou rolled a {user_wins_dice1} and {user_wins_dice2} which totals to {user_wins}") # using f string to format strings and using \n to break the line between strings
    print(f"CPU rolled a {CPU_wins_dice1} and {CPU_wins_dice2} which totals to {CPU_wins}")
    print("message")
    print(user_wins, CPU_wins)  # will say user wins and cpu wins
    break
input("Game Over")




