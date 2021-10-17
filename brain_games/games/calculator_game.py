# логика игры "калькулятор"
import random
import brain_games.general_logic as general_logic


def main():
    txt_greet = 'What is the result of the expression?'
    general_logic.enter_logic(txt_greet , questions)


def random_operator():
    operator_list = ['+', '-', '*']
    operator = operator_list[random.randint(0, 2)]
    return operator


def math_result(num_1, num_2, oper):
    if oper == '+':
        return num_1 + num_2
    elif oper == '-':
        return num_1 - num_2
    else:
        return num_1 * num_2


def questions():
    number_1 = random.randint(1, 100)
    number_2 = random.randint(1, 100)
    operator = random_operator()
    if number_1 > number_2:
        quest_txt = f'{number_1} {operator} {number_2}'
        try_answer = str(math_result(number_1, number_2, operator))
    else:
        quest_txt = f'{number_2} {operator} {number_1}'
        try_answer = str(math_result(number_2, number_1, operator))
    return [quest_txt, try_answer]


if __name__ == '__main__':
    main()
