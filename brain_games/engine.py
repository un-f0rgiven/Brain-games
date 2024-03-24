#!/usr/bin/env python3

def tell_rules(game):
    if game == 'brain_even':
        print('Answer "yes" if the number is even, otherwise answer "no".')
    elif game == 'brain_calc':
        print('What is the result of the expression?')
    elif game == 'brain_gcd':
        print('Find the greatest common divisor of given numbers.')
    elif game == 'brain-prime':
        print('Answer "yes" if given number is prime. Otherwise answer "no".')
    elif game == 'brain-progression':
        print('What number is missing in the progression?')


def check_answer(answer, correct_answer, player):
    if answer == str(correct_answer):
        print('Correct!')

    if answer != str(correct_answer):
        print(f'"{answer}" is wrong answer ;(. '
              f'Correct answer was "{correct_answer}".\n'
              f'Let\'s try again, {player}!'
              )
        exit()
