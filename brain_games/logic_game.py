import prompt
import random


def main():
    name = greeting()
    if logic_game() is True:
        print(f'Congratulations, {name}!')
    else:
        print(f"Let's try again, {name}")


def greeting():
    print('Welcome to the Brain Games!')
    name = prompt.string('May I have your name? ')
    print(f'Hello {name}')
    return name


def logic_game():
    print('Answer "yes" if the number is even, otherwise answer "no".')
    for i in range(3):
        return_list = questions()
        if return_list[0] is True:
            print('Correct')
        else:
            pr_1 = return_list[1]
            pr_2 = return_list[2]
            print(f"'{pr_1}' is wrong answer ;(. Correct answer was '{pr_2}'.")
            return(False)
    return True


def questions():
    number = random.randint(1, 100)
    print(f'Question: {number}')
    answer = prompt.string('Your answer: ')
    if number % 2 == 0 and answer == 'yes':
        return [True]
    elif number % 2 == 0 and answer == 'no':
        return [False, answer, 'yes']
    elif number % 2 != 0 and answer == 'no':
        return [True]
    else:
        return [False, answer, 'no']


if __name__ == '__main__':
    main()