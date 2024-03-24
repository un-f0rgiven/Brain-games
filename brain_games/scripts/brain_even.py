#!/usr/bin/env python3

import sys
sys.path.insert(0, '/home/alexander/python-project-49/brain_games')

import random

from engine import tell_rules
from engine import check_answer
from games.game_brain_even import brain_even

print("Welcome to the Brain Games!")
player = input('May I have your name? ')
print(f'Hello, {player}!')

game = 'brain_even'

tell_rules(game)

i = 1
while i < 4:

    a = random.randint(0, 100)

    question = a

    correct_answer = brain_even(a)

    print(f'Question: {question}')

    answer = input('Your answer: ')

    check_answer(answer, correct_answer, player)
    i = i + 1
else:
    print(f'Congratulations, {player}!')


def main():
    return ''


if __name__ == '__main__':
    main()
