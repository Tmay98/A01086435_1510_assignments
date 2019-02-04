"""
converts a phone number with letters in it to one with only numbers
"""

# Tommy May
# A01086435
# date

import doctest


def number_translator():
    """converts a phone number with letters in it to one with only numbers

    RETURN string with phone number converted to all numbers

    """
    entered_phone_number = input("Enter a phone number in the format XXX-XXX-XXXX: ")
    converted_number = ''

    # converts the 12 characters in the entered number one by one to numbers and returns the string
    converted_number = converted_number + (letter_converted_to_number(entered_phone_number[0]))
    converted_number = converted_number + (letter_converted_to_number(entered_phone_number[1]))
    converted_number = converted_number + (letter_converted_to_number(entered_phone_number[2]))
    converted_number = converted_number + (letter_converted_to_number(entered_phone_number[3]))
    converted_number = converted_number + (letter_converted_to_number(entered_phone_number[4]))
    converted_number = converted_number + (letter_converted_to_number(entered_phone_number[5]))
    converted_number = converted_number + (letter_converted_to_number(entered_phone_number[6]))
    converted_number = converted_number + (letter_converted_to_number(entered_phone_number[7]))
    converted_number = converted_number + (letter_converted_to_number(entered_phone_number[8]))
    converted_number = converted_number + (letter_converted_to_number(entered_phone_number[9]))
    converted_number = converted_number + (letter_converted_to_number(entered_phone_number[10]))
    converted_number = converted_number + (letter_converted_to_number(entered_phone_number[11]))
    return converted_number


def letter_converted_to_number(number_string):
    """converts a single character to the number it represents in a phone number

    PARAM: number_string a string
    PRECONDITION: number_string must be a 1 character long string
    POSTCONDITION: converts entered character to correct number
    RETURN: correctly converted character as a string

    >>> letter_converted_to_number('A')
    '2'
    >>> letter_converted_to_number('-')
    '-'
    >>> letter_converted_to_number('0')
    '0'

    """

    if number_string == 'A' or number_string == 'B' or number_string == 'C':
        return '2'
    elif number_string == 'D' or number_string == 'E' or number_string == 'F':
        return '3'
    elif number_string == 'G' or number_string == 'H' or number_string == 'I':
        return '4'
    elif number_string == 'J' or number_string == 'K' or number_string == 'L':
        return '5'
    elif number_string == 'M' or number_string == 'N' or number_string == 'O':
        return '6'
    elif number_string == 'P' or number_string == 'Q' or number_string == 'R' or number_string == 'S':
        return '7'
    elif number_string == 'T' or number_string == 'U' or number_string == 'V':
        return '8'
    elif number_string == 'W' or number_string == 'X' or number_string == 'Y' or number_string == 'Z':
        return '9'
    else:
        return number_string


def main():
    doctest.testmod()


if __name__ == '__main__':
    main()
