#!/usr/bin/env python3

from random import randint

description = 'Answer "yes" if the number is even, otherwise answer "no".'

def generate_game():
    n = randint(1, 50)
    question = str(n)
    right_answer = (n % 2 == 0) and 'yes' or 'no'
    return(question, right_answer)


if __name__ == '__main__':
    genrate_game()
