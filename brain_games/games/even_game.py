import random


TXT_GREET = 'Answer "yes" if the number is even, otherwise answer "no".'


def check_even(num):
    return num % 2 == 0


def give_question_answer():
    number = random.randint(1, 100)
    if check_even(number):
        try_answer = 'yes'
    else:
        try_answer = 'no'
    return [number, try_answer]
