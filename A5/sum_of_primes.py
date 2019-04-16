"""Function that returns sum of primes up to given number"""

# Tommy May
# A01086435

import math
import doctest


def sum_of_primes(number) -> int:
    """ calculates the sum of all primes up to a given number

    PARAM: number an int
    PRECONDITION: number must be a positive int
    POSTCONDITION: all prime numbers up to number are summed
    RETURN: the sum of all prime numbers up to given number

    >>> sum_of_primes(9)
    17
    >>> sum_of_primes(55)
    381
    """
    # raises an error if negative number is entered
    if number < 0:
        raise ValueError('only positive integers accepted as upper bounds')

    # creates initial primes lists with numbers as index and value as True
    primes = [True for value in range(number + 1)]

    # sets all non primes to False
    primes = set_non_primes(primes, number)

    sum_primes = 0
    for i in range(len(primes)):
        sum_primes += i if primes[i] is True else 0
    return sum_primes


def set_non_primes(primes, number):
    """sets all non prime indexes to False

    PARAM: number an int
    PRECONDITION: number must be a positive int
    PARAM: primes a list
    PARAM: primes must be a list
    RETURN: primes list with all non prime indexes set to False
    """
    if len(primes) > 1:
        primes[1] = False

    for i in range(2, math.floor(math.sqrt(number)) + 1):

        for j in range(2, i):
            if i % j == 0:
                primes[i] = False

        temp = i * 2
        while temp <= number:
            primes[temp] = False
            temp += i
    return primes


def main():
    doctest.testmod()
    print(sum_of_primes(9))


if __name__ == '__main__':
    main()
