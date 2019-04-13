"""cashmoney function converts an amount of money to the smallest number of bills  / coins"""

# Tommy May
# A01086435

import doctest


def cashmoney(amount: float) -> dict:
    """Converts an amount of money to its smallest amount of bills and coins

    PARAM: amount a float
    PRECONDITION: amount must be a positive float
    POSTCONDITION: the amount is seperated into minimum amount of bills / coins
    RETURN: the dictionary containing the amount of what bills / coins there are

    >>> cashmoney(265.52)
    {100: 2, 50: 1, 20: 0, 10: 1, 5: 1, 2: 0, 1: 0, 0.25: 2, 0.1: 0, 0.05: 0, 0.01: 2}
    """
    # raises ValueError if non-positive float entered
    if amount <= 0:
        raise ValueError('you did not enter a positive float')

    breakdown_dict = {100: 0, 50: 0, 20: 0, 10: 0, 5: 0, 2: 0, 1: 0, 0.25: 0, 0.10: 0, 0.05: 0, 0.01: 0}
    for key in breakdown_dict.keys():
        breakdown_dict[key] = int(amount // key)
        amount = round(amount % key, 2)
    return breakdown_dict


def main():
    doctest.testmod()
    print(cashmoney(123))


if __name__ == "__main__":
    main()
