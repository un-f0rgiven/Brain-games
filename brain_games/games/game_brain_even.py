#!/usr/bin/env python3
import random


def generate_round():
    a = random.randint(0, 100)

    question = a

    if a % 2 == 0:
        correct_answer = 'yes'
    else:
        correct_answer = 'no'

    return correct_answer, question


DESCRIPTION = 'Answer "yes" if the number is even, otherwise answer "no".'
