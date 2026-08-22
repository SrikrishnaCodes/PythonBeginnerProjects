from ggfinal import gg
from rpsfinal import rps
import sys


def play_arcade(name="PlayerOne"):
    welcomeback = False
    while True:
        if welcomeback == True:
            print(f"\n\nWelcome back to the Arcade, {name}! 🤖")
        decision = input(
            "\n\nPlease choose a game:\n1 = Rock Paper Scissors\n2 = Guess My Number\n\nOr press 'x' to exit the arcade\n\n")

        if decision not in ["1", "2", "x", "X"]:
            print(f"\n{name}, please enter 1, 2, or x.")
            return play_arcade(name)

        welcomeback = True

        if decision == "1":
            rock_paper_scissors = rps(name)
            rock_paper_scissors()
        elif decision == "2":
            guess_number = gg(name)
            guess_number()
        else:
            sys.exit(
                f"\n🎉🎉🎉🎉🎉🎉🎉\nThank you for playing at the arcade!\nBye, {name}!\n\n")


if __name__ == "__main__":
    import argparse
    parser = argparse.ArgumentParser(
        description="Personalised game experience"
    )
    parser.add_argument(
        "-n", "--name", metavar="name",
        required=True, help="Name of player"
    )
    args = parser.parse_args()
    print(f"\n\n{args.name}, Welcome to the Arcade! 🤖")
    play_arcade(args.name)
