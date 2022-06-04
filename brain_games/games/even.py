import random


TXT_GREET = 'Answer "yes" if the number is even, otherwise answer "no".'
START_RANDINT = 1
END_RANDINT = 100


def is_even(num):
    return num % 2 == 0


def get_question_answer():
    number = random.randint(START_RANDINT, END_RANDINT)
    if is_even(number):
        try_answer = 'yes'
    else:
        try_answer = 'no'
    return number, try_answer
