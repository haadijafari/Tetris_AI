from game import Game
import sys


def main():
    g = Game(sys.argv[1] if len(sys.argv) > 1 else None)
    g.run()


if __name__ == "__main__":
    main()