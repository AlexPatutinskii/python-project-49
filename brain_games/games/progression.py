#!/usr/bin/env python3


from random import randint


DESCRIPTION = 'What number is missing in the progression?'


def generate_game():
    first_n = randint(1, 30)
    delta = randint(2, 7)
    seq = list(range(first_n, first_n + delta * 10, delta))
    taken_element_position = randint(0, 9)
    right_answer = seq[taken_element_position]
    question = ''
    for i in range(10):
        if right_answer != seq[i]:
            question += str(seq[i])
            question += ' '
        else:
            question += '..'
            question += ' '
    return (str(question.strip()), str(right_answer))


if __name__ == '__main__':
    generate_game()
