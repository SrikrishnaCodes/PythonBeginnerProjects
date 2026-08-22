import sys
import random
from enum import Enum


def play_rps():
    class RPS(Enum):
        ROCK = 1
        PAPER = 2
        SCISSORS = 3

    playerchoice = input(
        "\nWelcome to Rock, Paper, Scissors.\n\nEnter...\n1 for Rock,\n2 for paper,\n3 for scissors.\n\n")

    if playerchoice not in ["1", "2", "3"]:
        print("\nYou must enter 1, 2, or 3!")
        return play_rps()

    player = int(playerchoice)
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

    print("\nPlay Again?")

    while True:
        playagain = input("\nY for Yes and \nQ to Quit \n\n")
        if playagain.lower() not in ["y", "q"]:
            continue
        else:
            break

    if playagain.lower() == "y":
        return play_rps()
    else:
        print('\n🎉🎉🎉🎉🎉')
        print('Thankyou For Playing!\n')
        sys.exit("Bye!👋\n")


play_rps()
