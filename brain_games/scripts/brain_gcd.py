from brain_games.games import gcd
from brain_games import general_logic as general


def main():
    general.starting_game(gcd, general.ROUNDS_COUNT)


if __name__ == '__main__':
    main()
