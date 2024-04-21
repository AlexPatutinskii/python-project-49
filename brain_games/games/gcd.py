#!/usr/bin/env python3

from random import randint
from math import gcd

description = 'Find the greatest common divisor of given numbers.'


def generate_game():
    first_n = randint(1, 50)
    second_n = randint(1, 50)
    question = f'{first_n} {second_n}'
    right_answer = gcd(first_n, second_n)
    return (question, str(right_answer))