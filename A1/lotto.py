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
    number_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23,
                   24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45,
                   46, 47, 48, 49]

    # creates a list of 6 random numbers between 1 and 49 then sorts it and returns
    lottery_numbers = random.sample(number_list, 6)
    lottery_numbers.sort()
    return lottery_numbers


def main():
    print(number_generator())


if __name__ == '__main__':
    main()







