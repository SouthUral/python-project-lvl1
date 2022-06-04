from brain_games.games import calculator
from brain_games import general_logic as general


def main():
    general.starting_game(calculator, general.ROUNDS_COUNT)


if __name__ == '__main__':
    main()
