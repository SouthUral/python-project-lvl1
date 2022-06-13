import random


RULES = "What number is missing in the progression?"
LOWER_BOUND_DIFF = 2
UPPER_BOUND_DIFF = 8
LOWER_BOUND_INIT = 1
UPPER_BOUND_INIT = 60
LOWER_BOUND_LEN = 5
UPPER_BOUND_LEN = 10


def make_progression(init_elem, step, length):
    progression = [
        init_elem,
    ]
    for i in range(length - 1):
        prev = progression[-1]
        progression.append(prev + step)
    return progression


def make_question_line(item_index, progression):
    progression[item_index] = ".."
    return " ".join(map(str, progression))


def get_question_answer():
    constant_difference = random.randint(LOWER_BOUND_DIFF, UPPER_BOUND_DIFF)
    init_element = random.randint(LOWER_BOUND_INIT, UPPER_BOUND_INIT)
    progression_length = random.randint(LOWER_BOUND_LEN, UPPER_BOUND_LEN)
    item_index = random.randint(0, progression_length - 1)
    progression = make_progression(
        init_element, constant_difference, progression_length
    )
    correct_answer = str(progression[item_index])
    question_line = make_question_line(item_index, progression)
    return question_line, correct_answer
