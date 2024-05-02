#!/usr/bin/env python3


from random import choice
from random import randint


DESCRIPTION = 'What is the result of the expression?'


def generate_game():
    first_n = randint(1, 10)
    second_n = randint(1, 10)
    operation_num = choice('+-*')
    match operation_num:
        case '+':
            question = f'{first_n} + {second_n}'
            right_answer = first_n + second_n
        case '-':
            question = f'{first_n} - {second_n}'
            right_answer = first_n - second_n
        case '*':
            question = f'{first_n} * {second_n}'
            right_answer = first_n * second_n
    return (str(question), str(right_answer))


if __name__ == '__main__':
    generate_game()
