"""
Converts an integer in the range 1 - 10 000 to its equivalent roman numeral
"""

# Tommy May
# A01086435
# date

import doctest


def convert_to_roman_numeral(positive_int):
    """Converts an integer in the range 1 - 10 000 to its equivalent roman numeral

    PARAM positive_int a positive integer
    PRE-CONDITION positive_int must be a positive integer
    RETURN a string with the roman numeral equivalent

    >>> convert_to_roman_numeral(1456)
    'MCDLVI'
    >>> convert_to_roman_numeral(0)
    ''
    >>> convert_to_roman_numeral(10000)
    'MMMMMMMMMM'
    >>> convert_to_roman_numeral(944)
    'CMXLIV'

    """
    converted_number = ''

    if positive_int >= 1000:
        converted_number = (positive_int // 1000) * 'M'
        positive_int = positive_int % 1000

    if 900 <= positive_int < 1000:
        converted_number = converted_number + 'CM'
        positive_int -= 900

    if positive_int >= 500:
        converted_number = converted_number + (positive_int // 500) * 'D'
        positive_int = positive_int % 500

    if 400 <= positive_int < 500:
        converted_number = converted_number + 'CD'
        positive_int -= 400

    if positive_int >= 100:
        converted_number = converted_number + (positive_int // 100) * 'C'
        positive_int = positive_int % 100

    if 90 <= positive_int < 100:
        converted_number = converted_number + 'XC'
        positive_int -= 90

    if positive_int >= 50:
        converted_number = converted_number +(positive_int // 50) * 'L'
        positive_int = positive_int % 50

    if 40 <= positive_int < 50:
        converted_number = converted_number + 'XL'
        positive_int -= 40

    if positive_int >= 10:
        converted_number = converted_number + (positive_int // 10) * 'X'
        positive_int = positive_int % 10

    if positive_int == 9:
        converted_number = converted_number + 'IX'
        positive_int -= 9

    if positive_int >= 5:
        converted_number = converted_number + 'V'
        positive_int = positive_int % 5

    if positive_int == 4:
        converted_number = converted_number + 'IV'
        positive_int -= 4

    if positive_int > 0:
        converted_number = converted_number + (positive_int * 'I')

    return converted_number


def main():
    doctest.testmod()


if __name__ == '__main__':
    main()
