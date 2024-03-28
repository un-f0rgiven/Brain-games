#!/usr/bin/env python3
import random


def generate_round():

    a = random.randint(1, 10)
    b = random.randint(0, 9)
    step = random.randint(1, 10)

    progression = [a]

    for x in range(1, 10):
        progression.append(a + x * step)

    first_question = ' '.join(map(str, progression[:b]))
    second_question = ' '.join(map(str, progression[b + 1:]))

    question = f'{first_question} .. {second_question}'

    correct_answer = progression[b]

    return correct_answer, question



