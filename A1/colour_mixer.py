"""
Takes 2 primary colours and prints the colour they create when combined
"""

# Tommy May
# A01086435
# date

import doctest


def colour_mixer():
    """ Takes 2 primary colours as user input and prints the colour they create when combined
    """

    # takes 2 colour inputs and normalizes them to lower case with no white space
    colour_1 = input("Enter the first primary colour to mix: ")
    colour_2 = input("Enter the second primary colour to mix: ")
    colour_1 = colour_1.strip()
    colour_2 = colour_2.strip()
    colour_1 = colour_1.lower()
    colour_2 = colour_2.lower()

    # calculates and prints the combined colour
    calculate_colour(colour_1, colour_2)
    return


def calculate_colour(colour_1, colour_2):
    """takes 2 primary colours and prints the resulting combined colour

    PARAM colour_1: a string
    PARAM colour_2: a string
    PRECONDITION colour_1 must be a string
    PRECONDITION colour_2 must be a string
    POSTCONDITION prints out resulting secondary colour

    >>> calculate_colour('blue', 'yellow')
    green
    >>> calculate_colour('blue', 'blue')
    You entered two of the same primary colour
    >>> calculate_colour('orange','turquoise')
    You did not enter two primary colours
    """

    # checks whether 2 primary colours were entered or not
    if ((colour_1 == 'blue' or colour_1 == 'yellow' or colour_1 == 'red')
            and (colour_2 == 'blue' or colour_2 == 'yellow' or colour_2 == 'red')):

        # calculates the different combinations of colours
        if (colour_1 == 'red' and colour_2 == 'blue') or (colour_1 == 'blue' and colour_2 == 'red'):
            print('purple')
        elif (colour_1 == 'red' and colour_2 == 'yellow') or (colour_1 == 'yellow' and colour_2 == 'red'):
            print('orange')
        elif (colour_1 == 'yellow' and colour_2 == 'blue') or (colour_1 == 'blue' and colour_2 == 'yellow'):
            print('green')
        else:
            print('You entered two of the same primary colour')
    # print error if 2 primary colours weren't entered
    else:
        print("You did not enter two primary colours")
    return


def main():
    doctest.testmod()


if __name__ == '__main__':
    main()

