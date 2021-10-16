# В данном модуле сгруппированы функции: приветствие, сравнение


import prompt


def greeting():
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
        print(f"Let's try again, {name}")
