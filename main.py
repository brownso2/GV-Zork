"""Main program for GV-ZORK.

Creates a Game object and starts the game.
"""

from game import Game


def main():
    """Creates a Game object and starts gameplay."""

    # Create the game object.
    game = Game()

    # Start the game.
    game.play()


if __name__ == "__main__":
    main()