#!/usr/bin/env python3
import random


def generate_round():
    a = random.randint(0, 100)
    b = random.randint(0, 100)

    question = f'{a} {b}'

    while a > 0 and b > 0:
        if a >= b:
            a = a % b
        else:
            b = b % a

    correct_answer = max(a, b)

    return correct_answer, question


DESCRIPTION = 'Find the greatest common divisor of given numbers.'
