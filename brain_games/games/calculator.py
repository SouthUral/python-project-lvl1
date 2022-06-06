# логика игры "калькулятор"
import random


RULES = 'What is the result of the expression?'
LOWER_BOUND = 1
UPPER_BOUND = 100


def get_math_result(num_1, num_2, oper):
    if oper == '+':
        return num_1 + num_2
    elif oper == '-':
        return num_1 - num_2
    else:
        return num_1 * num_2


def get_question_answer():
    numbers = [
        random.randint(LOWER_BOUND, UPPER_BOUND),
        random.randint(LOWER_BOUND, UPPER_BOUND)
    ]
    numbers.sort(reverse=True)
    operator = random.choice(['+', '-', '*'])
    quest_txt = f'{numbers[0]} {operator} {numbers[1]}'
    try_answer = str(get_math_result(*numbers, operator))
    return quest_txt, try_answer
