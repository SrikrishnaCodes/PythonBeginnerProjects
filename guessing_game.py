import random as rdm
import sys


def gg(name="PlayerOne"):
    game_count = 0
    player_wins = 0

    def play_gg():
        nonlocal name
        nonlocal game_count
        nonlocal player_wins

        playerchoice = input(
            f"\n\nHello {name}, guess which number im thinking of...\n1, 2, or 3.\n\n")

        if playerchoice not in ["1", "2", "3"]:
            print(f"\n{name}, please enter 1, 2, or 3!")
            return play_gg()

        player = int(playerchoice)
        computerchoice = rdm.choice("123")
        computer = int(computerchoice)
        print(f"\n{name} you guessed {playerchoice}.")
        print(f"I was thinking about the number {computerchoice}.\n")

        def decide_winner(player, computer):
            nonlocal player_wins
            if player == computer:
                player_wins += 1
                return f"Good job {name}, You guessed correctly! 🎉\n"
            else:
                return f"Sorry {name}, Better luck next time! 😢\n"

        game_result = decide_winner(player, computer)
        print(game_result)

        game_count += 1
        print(f"Game Count: {game_count}")
        print(f"\n{name}'s Wins: {player_wins}")
        print(
            f"\nYour Win Percentage = {player_wins/game_count:.2%}")

        print(f"\nPlay again, {name}?")

        while True:
            playagain = input("\nY for Yes or \nQ to Quit\n\n")
            if playagain.lower() not in ["y", "q"]:
                continue
            else:
                break

        if playagain.lower() == "y":
            return play_gg()
        else:
            print("\n🎉🎉🎉🎉🎉🎉🎉\nThanks for playing!")
            sys.exit(f"Bye, {name}! 👋\n")

    return play_gg


if __name__ == "__main__":
    import argparse
    parser = argparse.ArgumentParser(
        description="Provides personalised game experience."
    )
    parser.add_argument(
        "-n", "--name", metavar="name",
        required=True, help="Name of person playing the game."
    )
    args = parser.parse_args()
    guessing_game = gg(args.name)
    guessing_game()
