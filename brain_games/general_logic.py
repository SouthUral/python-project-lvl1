# В данном модуле сгруппированы функции: приветствие, сравнение


import prompt


def enter_logic(greet: str, quest):
    """Функция является связующей между логикой игр
       и основной логикой.
       Для использования функции нужно заполнить 2 аргумента
       greet - этот аргумент получает на вход строку с описанием игры
       quest - получает функцию с логикой игры, эта функция должна
       вернуть условие задачи в текстовом формате, и правильный ответ
    """
    # получаем имя пользователя
    name = greeting()
    print(greet)
    value_bool = logic_game(quest)
    end_game(name, value_bool)


def greeting():
    """Функция приветствия, выводит стандартное приветствие
       и запрашивает имя игрока, далее возвращает это имя
    """
    print('Welcome to the Brain Games!')
    name = prompt.string('May I have your name? ')
    print(f'Hello {name}')
    return name


def comparison(question, try_an):
    print(f'Question: {question}')
    an_r = prompt.string('Your answer: ')
    if an_r == try_an:
        print('Correct')
        return True
    else:
        a_s = f"'{an_r}' is wrong answer ;(. Correct answer was '{try_an}'."
        print(a_s)
        return False


def logic_game(def_game):
    """Функция 3 раза вызывает в цикле функцию с логикой игры,
       которая возвращает question - вопрос в текстовом формате,
       и try_answer - правильный ответ в текстовом формате
       Далее эти переменные передаются функции comparison,
       которая возвращает True или False
    """
    for i in range(3):
        question, try_answer = def_game()
        result = comparison(question, try_answer)
        if result is True:
            continue
        else:
            return False
    return True


def end_game(name, bool_return):
    if bool_return is True:
        print(f'Congratulations, {name}!')
    else:
        print(f"Let's try again, {name}!")
