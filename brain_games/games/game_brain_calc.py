#!/usr/bin/env python3
import random


def generate_round():
    a = random.randint(0, 100)
    b = random.randint(0, 100)
    operators = ['+', '-', '*']
    operation = operators[random.randint(0, 2)]

    question = f'{a} {operation} {b}'

    if operation == '+':
        correct_answer = a + b
    elif operation == '-':
        correct_answer = a - b
    elif operation == '*':
        correct_answer = a * b

    return correct_answer, question


DESCRIPTION = 'What is the result of the expression?'
