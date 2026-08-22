import sys
import random
from enum import Enum


class RPS(Enum):
    ROCK = 1
    PAPER = 2
    SCISSORS = 3


playagain = True
while playagain:
    playerchoice = input(
        "\nWelcome to Rock, Paper, Scissors.\n\nEnter...\n1 for Rock,\n2 for paper,\n3 for scissors.\n\n")
    player = int(playerchoice)

    if player < 1 or player > 3:
        sys.exit("You must enter 1, 2, or 3!")

    computerchoice = random.choice("123")
    computer = int(computerchoice)

    print("\nYou chose " + str(RPS(player)).replace('RPS.', '') + ".")
    print("Python chose " + str(RPS(computer)).replace('RPS.', '') + ".\n")

    if player == 1 and computer == 3:
        print("🎉 You Win!")
    elif player == 2 and computer == 1:
        print("🎉 You Win!")
    elif player == 3 and computer == 2:
        print("🎉 You Win!")
    elif player == computer:
        print("😑 Tie Game!")
    else:
        print("🐍 Python Wins!")

    playagain = input("\nPlay Again? \nY for Yes and \nQ to Quit \n\n")

    if playagain.lower() == "y":
        continue
    else:
        print('\n🎉🎉🎉🎉🎉')
        print('Thankyou For Playing!\n')
        playagain = False
        # break would also work

sys.exit("Bye!👋\n")
