# логика игры "арифметическая прогрессия"
import random
import brain_games.general_logic as general_logic


def main():
    txt_greet = 'What number is missing in the progression?'
    general_logic.enter_logic(txt_greet, progress_generation)


# генерируем последовательность прогрессии
def gen_list():
    step = random.randint(2, 8)
    start = random.randint(1, 60)
    length = random.randint(5, 10)
    prog_list = [start]
    for i in range(length - 1):
        prev = prog_list[-1]
        prog_list.append(prev + step)
    return [prog_list, length]


# генератор прогрессии
def progress_generation():
    prog_list, length = gen_list()
    index_elem = random.randint(0, length - 1)
    quest_list = list(map(str, prog_list))
    try_answer = quest_list[index_elem]
    quest_list[index_elem] = '..'
    quest_txt = ' '.join(quest_list)
    return [quest_txt, try_answer]


if __name__ == '__main__':
    main()
