# В данном модуле сгруппированы функции: приветствие, сравнение
import prompt


ROUNDS_COUNT = 3


def starting_game(game, number_of_rounds):
    """Функция является связующей между логикой игр
       и основной логикой.
       quest - получает функцию с логикой игры, эта функция должна
       вернуть условие задачи в текстовом формате, и правильный ответ
    """
    greet_game = game.TXT_GREET
    print('Welcome to the Brain Games!')
    name = prompt.string('May I have your name? ')
    print(f'Hello {name}')
    print(greet_game)
    for i in range(number_of_rounds):
        question, try_answer = game.get_question_answer()
        print(f'Question: {question}')
        answer_user = prompt.string('Your answer: ')
        if answer_user != try_answer:
            a_s = f"'{answer_user}' is wrong answer ;(. Correct answer was '{try_answer}'." # noqa
            print(a_s)
            print(f"Let's try again, {name}!")
            return
        print('Correct')
    print(f'Congratulations, {name}!')
