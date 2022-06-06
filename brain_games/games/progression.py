import random


RULES = 'What number is missing in the progression?'
LOWER_BOUND_DIFF = 2
UPPER_BOUND_DIFF = 8
LOWER_BOUND_INIT = 1
UPPER_BOUND_INIT = 60
LOWER_BOUND_LEN = 5
UPPER_BOUND_LEN = 10


def make_progression(init_elem, step, length):
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
    diff_const = random.randint(LOWER_BOUND_DIFF, UPPER_BOUND_DIFF)
    init_element = random.randint(LOWER_BOUND_INIT, UPPER_BOUND_INIT)
    len_prog = random.randint(LOWER_BOUND_LEN, UPPER_BOUND_LEN)
    del_item_index = random.randint(0, len_prog - 1)
    progress_list = make_progression(init_element, diff_const, len_prog)
    quest, answer = make_progress_str_try_answer(del_item_index, progress_list)
    return quest, answer
