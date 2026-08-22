def hello(name, lang):
    greeting = {
        'English': 'Hello',
        'Spanish': 'Hola',
        'German': 'Hallo'
    }
    msg = f"{greeting[lang]}, {name}!"
    print(msg)


if __name__ == "__main__":
    import argparse

    parser = argparse.ArgumentParser(
        description="Provides a personal greeting."
    )
    parser.add_argument(
        "-n", "--name", metavar="name",
        required=True, help="The name of person to greet."
    )
    parser.add_argument(
        "-l", "--lang", metavar="language",
        required=True, choices=["English", "Spanish", "German"],
        help="Language of greeting."
    )

    args = parser.parse_args()

    hello(args.name, args.lang)
