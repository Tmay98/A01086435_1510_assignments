"""
calculates compound interest given principal, interest rate,
 compounds per year, and number of years
"""

# Tommy May
# A01086435
# date

import doctest


def compound_interest(principal, annual_interest_rate, compounds_per_year, number_of_years):
    """ calculates compound interest given principal, interest rate,
    compounds per year, and number of years

    PARAM principal a float
    PARAM annual_interest_rate a float
    PARAM compounds_per_year an int
    PARAM number_of_years an int
    PRE-CONDITION annual_interest_rate must be a float
    PRE-CONDITION compounds_per_year must be an float
    PRE-CONDITION compound_per_year must be an int
    PRE-CONDITION number_of_years must be an int
    RETURN money_in_account after entered amount of years

    >>> compound_interest(100, 0.10, 4, 10)
    268.5063838389963
    >>> compound_interest(0, 0.10, 6, 20)
    0.0
    >>> compound_interest(200, 0, 5, 15)
    200.0
    """

    money_in_account = principal*((1+(annual_interest_rate/compounds_per_year))**(compounds_per_year*number_of_years))
    return money_in_account


def main():
    doctest.testmod()


if __name__ == '__main__':
    main()

