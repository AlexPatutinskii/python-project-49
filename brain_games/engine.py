#!/usr/bin/env python3

def run_game(game):
    print('Welcome to the Brain Games!')
    user_name = input('May I have your name? ')
    print(game.description)
    question, right_answer = game.generate_game()
    counter = 0
    while counter < 3:
        question, right_answer = game.generate_game()
        print(f'Question: {question}')
        user_answer = input('Your answer: ')
        if user_answer == right_answer:
            print('Correct!')
            counter += 1
        else:
            print(f"'{user_answer}' is wrong answer ;(. ", end='')
            print(f"Correct answer was '{right_answer}'.")
            print(f"Let's try again, {user_name}!")
            break
        if counter == 3:
            print(f"Congratulations, {user_name}!")


if __name__ == '__main__':
    run_game()
