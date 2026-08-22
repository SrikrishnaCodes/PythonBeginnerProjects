import sys
import random
from enum import Enum


def rps():
    game_count = 0
    player_wins = 0
    python_wins = 0

    def play_rps():

        nonlocal player_wins
        nonlocal python_wins

        class RPS(Enum):
            ROCK = 1
            PAPER = 2
            SCISSORS = 3

        playerchoice = input(
            "\n\n\nWelcome to Rock, Paper, Scissors.\n\nEnter...\n1 for Rock,\n2 for paper,\n3 for scissors.\n\n")

        if playerchoice not in ["1", "2", "3"]:
            print("\nYou must enter 1, 2, or 3!")
            return play_rps()

        player = int(playerchoice)
        computerchoice = random.choice("123")
        computer = int(computerchoice)

        print("\nYou chose " + str(RPS(player)).replace('RPS.', '') + ".")
        print("Python chose " + str(RPS(computer)).replace('RPS.', '') + ".\n")

        def decide_winner(player, computer):
            nonlocal player_wins
            nonlocal python_wins
            if player == 1 and computer == 3:
                player_wins += 1
                return "🎉 You Win!"
            elif player == 2 and computer == 1:
                player_wins += 1
                return "🎉 You Win!"
            elif player == 3 and computer == 2:
                player_wins += 1
                return "🎉 You Win!"
            elif player == computer:
                return "😑 Tie Game!"
            else:
                python_wins += 1
                return "🐍 Python Wins!"

        game_result = decide_winner(player, computer)
        print(game_result)

        nonlocal game_count
        game_count += 1
        print("\nGame Count: " + str(game_count))
        print("\nPlayer Wins: " + str(player_wins))
        print("\nPython Wins: " + str(python_wins))

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

    return play_rps


play = rps()
play()
