#!/usr/bin/env python3

from random import randint
import prompt


def main():
    print('Welcome to the Brain Games!')
    user_name = prompt.string('May I have your name? ')
    print('Answer "yes" if the number is even, otherwise answer "no".')
    counter = 0
    while counter < 3:
        n = randint(1, 50)
        print(f'Question: {n}')
        user_answer = prompt.string('Your answer: ')
        right_answer = (n % 2 == 0) and 'yes' or 'no'
        if user_answer == right_answer:
            counter += 1
            print('Correct!')
        else:
            counter = 10
            print(f"'{user_answer}' is wrong answer ;(. Correct answer was '{right_answer}'.")
            print(f"Let's try again, {user_name}!")
    if counter == 3:
        print(f"Congratulations, {user_name}!")


if __name__ == '__main__':
    main()
