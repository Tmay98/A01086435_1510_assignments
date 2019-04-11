"""Base conversion function to convert from one base to another"""

# Tommy May
# A01086435

import doctest


def base_conversion(base_from, number: int, base_to):
    """ Converts a number from one base to another

    PARAM: base_from an int
    PRECONDITION: base_from must be an int between 2 and 10
    PARAM: number an int
    PRECONDITION: number must be a positive integer
    PARAM: base_to an int
    PRECONDITION: base_to must be an int between 2 and 10
    POSTCONDITION: number is converted to desired base
    RETURN: number in desired base

    >>> base_conversion(10, 256, 2)
    100000000
    >>> base_conversion(2, 100000000, 10)
    256
    """
    base_10_number = 0
    digits_list = [int(digit) for digit in str(number)]
    converted_number_list = []

    # convert number to base 10
    for i in range(len(digits_list)):
        base_10_number += digits_list[len(digits_list) - 1 - i] * base_from ** i

    # converts number to desired base from base 10
    while base_10_number > 0:
        converted_number_list.append(base_10_number % base_to)
        base_10_number = base_10_number // base_to
    converted_number_list.reverse()
    # converts list to string and makes it an integer
    converted_number = int(''.join(str(i) for i in converted_number_list))
    return converted_number


def main():
    doctest.testmod()
    print(base_conversion(10, 256, 2))


if __name__ == '__main__':
    main()



