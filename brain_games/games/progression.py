import random


TXT_GREET = 'What number is missing in the progression?'
START_DIFF_CONST = 2
END_DIFF_CONST = 8
START_INIT_ELEMENT = 1
END_INIT_ELEMENT = 60
START_LEN_PROG = 5
END_LEN_PROG = 10


def int_progress_generation(init_elem, step, length):
    progress_list = [init_elem, ]
    for i in range(length - 1):
        prev = progress_list[-1]
        progress_list.append(prev + step)
    return progress_list


def make_progress_str_try_answer(item_index, prog_list):
    progress_list_str = list(map(str, prog_list))
    try_answer = progress_list_str[item_index]
    progress_list_str[item_index] = '..'
    progress_txt = ' '.join(progress_list_str)
    return progress_txt, try_answer


def get_question_answer():
    diff_const = random.randint(START_DIFF_CONST, END_DIFF_CONST)
    init_element = random.randint(START_INIT_ELEMENT, END_INIT_ELEMENT)
    len_prog = random.randint(START_LEN_PROG, END_LEN_PROG)
    del_item_index = random.randint(0, len_prog - 1)
    progress_list = int_progress_generation(init_element, diff_const, len_prog)
    quest, answer = make_progress_str_try_answer(del_item_index, progress_list)
    return quest, answer
