#!/usr/bin/env python3

from random import randint

description = 'What is the result of the expression?'

def generate_game():
    first_n = randint(1, 10)
    second_n = randint(1, 10)
    operation = ['+', '-', '*']
    operation_num = randint(0, 2)
    match operation_num:
        case 0:
            question = f'{first_n} + {second_n}'
            right_answer = first_n + second_n
        case 1:
            question = f'{first_n} - {second_n}'
            right_answer = first_n - second_n
        case 2:
            question = f'{first_n} * {second_n}'
            right_answer = first_n * second_n
    return (str(question), str(right_answer))


if __name__ == '__main__':
    generate_game()
