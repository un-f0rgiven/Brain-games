#!/usr/bin/env python3
from brain_games.engine import run_game
from brain_games.games import game_brain_gcd


def main():
    print("Welcome to the Brain Games!")


run_game(game_brain_gcd)

if __name__ == "__main__":
    main()
