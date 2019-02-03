"""
Converts seconds to a list with days, hours, minutes, and seconds
"""

# Tommy May
# A01086435
# date

import doctest


def time_calculator(entered_seconds):
    """takes the amount of seconds entered and returns it as days, hours, minutes, and seconds

    PARAM entered_seconds a positive int
    PRE-CONDITION entered_seconds must be a positive int
    RETURN a list with seconds converted to days, hours, minutes, seconds

    >>> time_calculator(92566)
    ['days', 1, 'hours', 1, 'minutes', 42, 'seconds', 46]
    >>> time_calculator(-5)
    You did not enter a positive integer
    >>> time_calculator(0)
    ['days', 0, 'hours', 0, 'minutes', 0, 'seconds', 0]
    """
    days = 0
    hours = 0
    minutes = 0
    seconds = 0
    time_list = ['days', days, 'hours', hours, 'minutes', minutes, 'seconds', seconds]
    if entered_seconds < 0:
        print('You did not enter a positive integer')
        return
    # calculates amount of days and subtracts from seconds
    if entered_seconds >= 86400:
        time_list[1] = entered_seconds // 86400
        entered_seconds = entered_seconds % 86400

    # calculates amount of hours and subtracts from seconds
    if entered_seconds >= 3600:
        time_list[3] = entered_seconds // 3600
        entered_seconds = entered_seconds % 3600

    # calculates amount of minutes and subtracts from seconds
    if entered_seconds >= 60:
        time_list[5] = entered_seconds // 60
        entered_seconds = entered_seconds % 60

    # takes final amount as seconds
    if entered_seconds > 0:
        time_list[7] = entered_seconds

    return time_list


def main():
    doctest.testmod()


if __name__ == '__main__':
    main()
