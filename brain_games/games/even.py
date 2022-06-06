import random


RULES = 'Answer "yes" if the number is even, otherwise answer "no".'
LOWER_BOUND = 1
UPPER_BOUND = 100


def is_even(num):
    return num % 2 == 0


def get_question_answer():
    number = random.randint(LOWER_BOUND, UPPER_BOUND)
    if is_even(number):
        try_answer = 'yes'
    else:
        try_answer = 'no'
    return number, try_answer
