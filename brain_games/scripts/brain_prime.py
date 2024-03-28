#!/usr/bin/env python3
from brain_games.engine import run_game
import brain_games.games.game_brain_prime

import sys
sys.path.insert(0, '/home/alexander/python-project-49')


def main():
    return "Welcome to the Brain Games!"


run_game(brain_games.games.game_brain_prime)

if __name__ == "__main__":
    main()
