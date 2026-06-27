"""Main file for GV-ZORK. Starts the game."""

from game import Game


def main():
    """Creates and starts the game."""

    game = Game()
    game.play()

    print("Game created successfully.")


if __name__ == "__main__":
    main()