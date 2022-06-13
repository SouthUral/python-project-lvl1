# В данном модуле сгруппированы функции: приветствие, сравнение
import prompt


ROUNDS_COUNT = 3


def game_engine(game, number_of_rounds):
    """Функция является связующей между логикой игр
       и основной логикой.
       quest - получает функцию с логикой игры, эта функция должна
       вернуть условие задачи в текстовом формате, и правильный ответ
    """
    game_rules = game.RULES
    print('Welcome to the Brain Games!')
    name = prompt.string('May I have your name? ')
    print(f'Hello {name}')
    print(game_rules)
    for i in range(number_of_rounds):
        question, correct_answer = game.get_question_answer()
        print(f'Question: {question}')
        user_answer = prompt.string('Your answer: ')
        if user_answer != correct_answer:
            a_s = f"'{user_answer}' is wrong answer ;(. Correct answer was '{correct_answer}'." # noqa
            print(a_s)
            print(f"Let's try again, {name}!")
            return
        print('Correct')
    print(f'Congratulations, {name}!')
