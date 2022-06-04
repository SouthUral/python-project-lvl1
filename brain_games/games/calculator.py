# логика игры "калькулятор"
import random


TXT_GREET = 'What is the result of the expression?'
START_RANDINT = 1
END_RANDINT = 100


def get_math_result(num_1, num_2, oper):
    if oper == '+':
        return num_1 + num_2
    elif oper == '-':
        return num_1 - num_2
    else:
        return num_1 * num_2


def get_question_answer():
    numbers = [
        random.randint(START_RANDINT, END_RANDINT),
        random.randint(START_RANDINT, END_RANDINT)
    ]
    numbers.sort(reverse=True)
    operator = random.choice(['+', '-', '*'])
    quest_txt = f'{numbers[0]} {operator} {numbers[1]}'
    try_answer = str(get_math_result(*numbers, operator))
    return quest_txt, try_answer
