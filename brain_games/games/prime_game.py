# логика игры brain-prime
import random


TXT_GREET = 'Answer "yes" if given number is prime. Otherwise answer "no".'


def check_prime(num):
    return 'yes' if is_simple(num) else 'no'


def is_simple(num):
    for i in range(2, num):
        if num % i == 0:
            return False
    return True


def give_question_answer():
    quest_num = random.randint(1, 100)
    try_answer = check_prime(quest_num)
    quest_txt = str(quest_num)
    return [quest_txt, try_answer]
