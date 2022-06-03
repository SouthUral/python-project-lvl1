# логика игры "калькулятор"
import random


TXT_GREET = 'What is the result of the expression?'


def math_result(num_1, num_2, oper):
    if oper == '+':
        return num_1 + num_2
    elif oper == '-':
        return num_1 - num_2
    else:
        return num_1 * num_2


def give_question_answer():
    numbers = [random.randint(1, 100), random.randint(1, 100)]
    numbers.sort(reverse=True)
    operator = ['+', '-', '*'][random.randint(0, 2)]
    quest_txt = f'{numbers[0]} {operator} {numbers[1]}'
    try_answer = str(math_result(*numbers, operator))
    return [quest_txt, try_answer]
