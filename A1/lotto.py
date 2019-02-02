"""
creates 6 random numbers between 1 and 49 and sorts them from lowest to highest in a list
"""

# Tommy May
# A01086435
# date

import random


def number_generator():
    """ creates 6 random numbers between 1 and 49 and sorts them from lowest to highest in a list

    RETURN a sorted list of 6 numbers between 1 and 49
    """
    lottery_numbers = random.sample(range(50), 6)
    lottery_numbers.sort()
    return lottery_numbers


def main():
    print(number_generator())


if __name__ == '__main__':
    main()







