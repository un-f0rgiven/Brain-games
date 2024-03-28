#!/usr/bin/env python3


def main():
    print("Welcome to the Brain Games!")


def run_game(game):
    player = input('May I have your name? ')

    print(f'Hello, {player}!')

    print(game.DESCRIPTION)

    i = 1
    while i < 4:

        correct_answer, question = game.generate_round()

        game.generate_round()

        print(f'Question: {question}')

        answer = input('Your answer: ')

        if answer == str(correct_answer):
            print('Correct!')
        if answer != str(correct_answer):
            print(f'"{answer}" is wrong answer ;(. '
                  f'Correct answer was "{correct_answer}".\n'
                  f'Let\'s try again, {player}!'
                  )
            exit()
        i = i + 1
    else:
        print(f'Congratulations, {player}!')


if __name__ == "__main__":
    main()
