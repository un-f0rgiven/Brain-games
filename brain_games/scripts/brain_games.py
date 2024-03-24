#!/usr/bin/env python3

from brain_games.cli import welcome_user


def greeting():
    print("Welcome to the Brain Games!")
    print("Hello, " + welcome_user() + "!")


def main():
    greeting()


if __name__ == "__main__":
    main()
