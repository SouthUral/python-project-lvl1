# логика игры "арифметическая прогрессия"
import random


TXT_GREET = 'What number is missing in the progression?'


# генерируем последовательность прогрессии
def gen_list(init_elem, step, length):
    prog_list = [init_elem, ]
    for i in range(length - 1):
        prev = prog_list[-1]
        prog_list.append(prev + step)
    return prog_list


# генератор прогрессии
def progress_generation(item_index, prog_list):
    quest_list = list(map(str, prog_list))
    try_answer = quest_list[item_index]
    quest_list[item_index] = '..'
    quest_txt = ' '.join(quest_list)
    return quest_txt, try_answer


def give_question_answer():
    diff_const = random.randint(2, 8)
    init_element = random.randint(1, 60)
    len_prog = random.randint(5, 10)
    del_item_index = random.randint(0, len_prog - 1)
    progression_list = gen_list(init_element, diff_const, len_prog)
    quest, answer = progress_generation(del_item_index, progression_list)
    return quest, answer
