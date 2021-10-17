import random
import brain_games.general_logic as general_logic


def main():
    txt_greet = 'Answer "yes" if the number is even, otherwise answer "no".'
    # вызываем функцию, которая является точкой входа в основную логику
    # на вход передаем текст с приветствием текущей игры, и функцию
    # с логикой игры
    general_logic.enter_logic(txt_greet, questions)


def questions():
    number = random.randint(1, 100)
    if number % 2 == 0:
        try_answer = 'yes'
    else:
        try_answer = 'no'
    return [number, try_answer]


if __name__ == '__main__':
    main()
