"""gcd calculator function calculates the gcd of 2 integers"""

# Tommy May
# A01086435

from math import floor
import doctest


def gcd(a: int, b: int):
    """ Calculates the gcd of 2 integers

    PARAM: a an int
    PRECONDITION: a must be an int
    PARAM: b an int
    PRECONDITION: b must be an int
    POSTCONDITION: gcd of a and b is calculated
    RETURN: gcd of a and b

    >>> gcd(25, 15)
    5
    >>> gcd(15, -25)
    5
    """
    if a == 0:
        return abs(b)
    elif b == 0:
        return abs(a)
    else:
        return gcd(b, a - b * floor(a / b))


def main():
    doctest.testmod()
    print(gcd(-25, 15))


if __name__ == '__main__':
    main()
