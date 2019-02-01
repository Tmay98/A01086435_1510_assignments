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

    """
    converted_number = ''
    if positive_int >= 1000:
        converted_number = converted_number + 'M' + (convert_to_roman_numeral(positive_int - 1000))
        return converted_number

    elif 900 <= positive_int < 1000:
        converted_number = converted_number + 'CM' + (convert_to_roman_numeral(positive_int - 900))
        return converted_number

    elif positive_int >= 500:
        converted_number = converted_number + 'D' + (convert_to_roman_numeral(positive_int - 500))
        return converted_number

    elif 400 <= positive_int < 500:
        converted_number = converted_number + 'CD' + (convert_to_roman_numeral(positive_int - 400))
        return converted_number

    elif positive_int >= 100:
        converted_number = converted_number + 'C' + (convert_to_roman_numeral(positive_int - 100))
        return converted_number

    elif 90 <= positive_int < 100:
        converted_number = converted_number + 'XC' + (convert_to_roman_numeral(positive_int - 90))
        return converted_number

    elif positive_int >= 50:
        converted_number = converted_number + 'L' + (convert_to_roman_numeral(positive_int - 50))
        return converted_number

    elif 40 <= positive_int < 50:
        converted_number = converted_number + 'XL' + (convert_to_roman_numeral(positive_int - 40))
        return converted_number

    elif positive_int >= 10:
        converted_number = converted_number + 'X' + (convert_to_roman_numeral(positive_int - 10))
        return converted_number

    elif positive_int == 9:
        converted_number = converted_number + 'IX' + (convert_to_roman_numeral(positive_int - 9))
        return converted_number

    elif positive_int >= 5:
        converted_number = converted_number + 'V' + (convert_to_roman_numeral(positive_int - 5))
        return converted_number

    elif positive_int == 4:
        return 'IV'
    elif positive_int == 3:
        return 'III'
    elif positive_int == 2:
        return 'II'
    elif positive_int == 1:
        return 'I'
    elif positive_int == 0:
        return ''


def main():
    doctest.testmod()


if __name__ == '__main__':
    main()
