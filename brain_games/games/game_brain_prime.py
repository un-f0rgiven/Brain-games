#!/usr/bin/env python3

def brain_prime(a, divisors):
    for element in divisors:
        if a % element == 0:
            return "no"
    return "yes"
