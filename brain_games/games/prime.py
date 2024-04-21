#!/usr/bin/env python3

from random import randint
from math import sqrt

description = 'Answer "yes" if given number is prime. Otherwise answer "no".'

def generate_game():
    first_n = randint(1, 100)
    question = first_n
    right_answer = 'yes'
    if first_n in [1, 2, 3]:
        return (str(question), str(right_answer))
    for elem in range(2,int(sqrt(first_n)) + 1):
        if first_n % elem == 0:
            right_answer = 'no'
            break

    return (str(question), str(right_answer))


if __name__ == '__main__':
    generate_game()
