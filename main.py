from snakes_and_ladders import game


def main() -> None:
    """Runs snakes and ladders game."""
    start = 0
    end = 99
    snakes = {
        16: 6,
        48: 26,
        49: 11,
        56: 53,
        62: 19,
        64: 60,
        87: 24,
        93: 73,
        95: 75,
        98: 78,
    }
    ladders = {
        1: 38,
        4: 14,
        9: 31,
        21: 42,
        28: 84,
        36: 44,
        51: 67,
        71: 91,
        80: 99,
    }

    number_of_steps = game.find_minimum_number_of_steps(start, end, snakes, ladders)

    print("Minimum number of steps to win the game is:", number_of_steps)


# prevents execution of main function when importing main.py in other files
if __name__ == "__main__":
    main()
