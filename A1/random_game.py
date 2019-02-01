"""
Play rock paper scissors with the computer
"""

# Tommy May
# A01086435
# date

import random


def rock_paper_scissors():
    """play rock paper scissors with the computer
    """

    computer_guess = random.randint(0, 2)

    if computer_guess == 0:
        computer_guess = 'rock'
    elif computer_guess == 1:
        computer_guess = 'paper'
    else:
        computer_guess = 'scissors'

    user_guess = input("Enter either rock, paper, or scissors: ")
    user_guess = user_guess.strip()
    user_guess = user_guess.lower()

    if not(user_guess == 'rock' or user_guess == 'paper' or user_guess == 'scissors'):
        print("you did not enter rock, paper, or scissors")
    elif user_guess == 'rock' and computer_guess == 'scissors':
        print('The computer guessed scissors, You won!')
    elif user_guess == 'paper' and computer_guess == 'rock':
        print('The computer guessed rock, You won!')
    elif user_guess == 'scissors' and computer_guess == 'paper':
        print('The computer guessed paper, You won!')
    elif user_guess == 'rock' and computer_guess == 'paper':
        print('The computer guessed paper, You lost!')
    elif user_guess == 'paper' and computer_guess == 'scissors':
        print('The computer guessed scissors, You lost!')
    elif user_guess == 'scissors' and computer_guess == 'rock':
        print('The computer guessed rock, You lost!')
    else:
        print('You tied!')


def main():
    rock_paper_scissors()


if __name__ == '__main__':
    main()



