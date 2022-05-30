# логика игры brain-prime
import random


def prime_game():
    txt_greet = 'Answer "yes" if given number is prime. Otherwise answer "no".'
    return txt_greet, prime


def check_prime(num):
    for i in range(2, num):
        if num % i == 0:
            return 'no'
    return 'yes'


def prime():
    quest_num = random.randint(59, 61)
    try_answer = check_prime(quest_num)
    quest_txt = str(quest_num)
    return [quest_txt, try_answer]
