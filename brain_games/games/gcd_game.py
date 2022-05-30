import random


def gcd_game():
    txt_greet = 'Find the greatest common divisor of given numbers.'
    return txt_greet, questions


def gcd(nums_list):
    nums_list.sort()
    num_1, num_2 = nums_list
    div_list = [i for i in range(1, num_1 + 1)]
    general_div_list = []
    for n in div_list:
        if num_1 % n == 0 and num_2 % n == 0:
            general_div_list.append(n)
    general_div_list.sort()
    return general_div_list[-1]


def questions():
    num_list = rundom_nums()
    try_answer = str(gcd(num_list))
    quest_txt = f'{num_list[0]} {num_list[1]}'
    return [quest_txt, try_answer]


def rundom_nums():
    num_1 = random.randint(1, 100)
    num_2 = random.randint(1, 100)
    return [num_1, num_2]
