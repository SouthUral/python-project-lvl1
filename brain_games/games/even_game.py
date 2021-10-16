import random
import brain_games.general_logic as general_logic


def main():
    name = general_logic.greeting()
    print('Answer "yes" if the number is even, otherwise answer "no".')
    value_bool = general_logic.logic_game(questions)
    general_logic.end_game(name, value_bool)


def questions():
    number = random.randint(1, 100)
    if number % 2 == 0:
        try_answer = 'yes'
    else:
        try_answer = 'no'
    return [number, try_answer]


if __name__ == '__main__':
    main()
