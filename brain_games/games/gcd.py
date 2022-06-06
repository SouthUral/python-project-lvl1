import random


RULES = 'Find the greatest common divisor of given numbers.'
LOWER_BOUND = 1
UPPER_BOUND = 100


def gcd(a, b):
    while b > 0:
        a, b = b, a % b
    return a


def get_question_answer():
    num_list = [
        random.randint(LOWER_BOUND, UPPER_BOUND),
        random.randint(LOWER_BOUND, UPPER_BOUND)
    ]
    num_list.sort()
    try_answer = str(gcd(*num_list))
    quest_txt = f'{num_list[0]} {num_list[1]}'
    return quest_txt, try_answer
