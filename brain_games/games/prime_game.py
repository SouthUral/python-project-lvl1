# логика игры brain-prime
import random
import brain_games.general_logic as general


def main():
    txt_greet = 'Answer "yes" if given number is prime. Otherwise answer "no".'
    general.enter_logic(txt_greet, prime)


def check_prime(num):
    for i in range(2, num):
        if num % i == 0:
            return 'no'
    return 'yes'


def prime():
    quest_num = random.randint(1, 200)
    try_answer = check_prime(quest_num)
    quest_txt = str(quest_num)
    return [quest_txt, try_answer]


if __name__ == '__main__':
    main()
