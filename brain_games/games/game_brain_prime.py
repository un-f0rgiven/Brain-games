#!/usr/bin/env python3
import random
import math


def brain_prime(a, divisors):
    for element in divisors:
        if a % element == 0:
            return "no"
    return "yes"


def generate_round():
    a = random.randint(2, 100)
    a_sqrt = int(math.sqrt(a))
    divisors = range(2, (a_sqrt + 1))

    question = a

    correct_answer = brain_prime(a, divisors)

    return correct_answer, question


DESCRIPTION = 'Answer "yes" if given number is prime. Otherwise answer "no".'
