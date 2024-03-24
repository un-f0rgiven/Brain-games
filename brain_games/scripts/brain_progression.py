#!/usr/bin/env python3

import sys
sys.path.insert(0, '/home/alexander/python-project-49/brain_games')

import random

from engine import tell_rules
from engine import check_answer
from games.game_brain_progression import brain_progression

print("Welcome to the Brain Games!")
player = input('May I have your name? ')
print(f'Hello, {player}!')

game = 'brain_progression'

tell_rules(game)

i = 1
while i < 4:

    a = random.randint(1, 10)
    b = random.randint(0, 9)
    step = random.randint(1, 10)

    progression = [a]

    for x in range(1, 10):
        progression.append(a + x * step)

    first_question = ' '.join(map(str, progression[:b]))
    second_question = ' '.join(map(str, progression[b + 1:]))

    question = f'{first_question} .. {second_question}'

    correct_answer = brain_progression(b, progression)

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