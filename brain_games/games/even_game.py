import random


def even_game():
    txt_greet = 'Answer "yes" if the number is even, otherwise answer "no".'
    return txt_greet, questions


def questions():
    number = random.randint(1, 100)
    if number % 2 == 0:
        try_answer = 'yes'
    else:
        try_answer = 'no'
    return [number, try_answer]
