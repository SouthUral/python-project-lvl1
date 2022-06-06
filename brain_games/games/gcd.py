import random


RULES = 'Find the greatest common divisor of given numbers.'
LOWER_BOUND = 1
UPPER_BOUND = 100


def gcd(num_1, num_2):
    div_list = [i for i in range(1, num_1 + 1)]
    general_div_list = []
    for n in div_list:
        if num_1 % n == 0 and num_2 % n == 0:
            general_div_list.append(n)
    return max(general_div_list)


def get_question_answer():
    num_list = [
        random.randint(LOWER_BOUND, UPPER_BOUND),
        random.randint(LOWER_BOUND, UPPER_BOUND)
    ]
    num_list.sort()
    try_answer = str(gcd(*num_list))
    quest_txt = f'{num_list[0]} {num_list[1]}'
    return quest_txt, try_answer
