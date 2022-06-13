from brain_games.games import even
from brain_games import general_logic as general


def main():
    general.game_engine(even, general.ROUNDS_COUNT)


if __name__ == '__main__':
    main()
