"""
Converts seconds to a list with days, hours, minutes, and seconds
"""

# Tommy May
# A01086435
# date

import doctest


def time_calculator(entered_seconds):
    """takes the amount of seconds entered and returns it as days, hours, minutes, and seconds

    PARAM entered_seconds an int
    PRE-CONDITION entered_seconds must be an int
    RETURN a list with seconds converted to days, hours, minutes, seconds

    >>> time_calculator(92566)
    ['days', 1, 'hours', 1, 'minutes', 42, 'seconds', 46]
    >>> time_calculator(0)
    ['days', 0, 'hours', 0, 'minutes', 0, 'seconds', 0]


    """
    days = 0
    hours = 0
    minutes = 0
    seconds = 0
    time_list = ['days', days, 'hours', hours, 'minutes', minutes, 'seconds', seconds]
    if entered_seconds >= 86400:
        time_list = time_calculator(entered_seconds - 86400)
        time_list[1] += 1
    elif entered_seconds >= 3600:
        time_list = time_calculator(entered_seconds - 3600)
        time_list[3] += 1
    elif entered_seconds >= 60:
        time_list = time_calculator(entered_seconds - 60)
        time_list[5] += 1
    else:
        time_list[7] = entered_seconds
    return time_list


def main():
    doctest.testmod()


if __name__ == '__main__':
    main()
