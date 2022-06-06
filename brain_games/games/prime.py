# логика игры brain-prime
import random


RULES = 'Answer "yes" if given number is prime. Otherwise answer "no".'
LOWER_BOUND = 1
UPPER_BOUND = 100


def check_prime(num):
    return 'yes' if is_prime(num) else 'no'


def is_prime(num):
    for i in range(2, num):
        if num % i == 0:
            return False
    return True


def get_question_answer():
    quest_num = random.randint(LOWER_BOUND, UPPER_BOUND)
    try_answer = check_prime(quest_num)
    quest_txt = str(quest_num)
    return quest_txt, try_answer
