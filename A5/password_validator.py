"""Password validator function to check if a password is strong"""

# Tommy May
# A01086435

import re
import doctest


def password_validator(password: str) -> bool:
    """ checks if a password contains upper and lowercase letters, a number, and is at least 8 characters long

    PARAM: password a string
    PRECONDITION: password must be a string
    POSTCONDITION: checks if the password is strong enough
    RETURN: False if password not strong, True if it is strong

    >>> password_validator('geefgG23f')
    True
    >>> password_validator('badpassword')
    False
    """

    length_regex = re.compile(r'.{8,}')
    upper_case_regex = re.compile(r'.*[A-Z].*')
    lower_case_regex = re.compile(r'.*[a-z].*')
    number_regex = re.compile(r'.*\d.*')

    match_object_1 = upper_case_regex.search(password)
    match_object_2 = lower_case_regex.search(password)
    match_object_3 = length_regex.search(password)
    match_object_4 = number_regex.search(password)

    if match_object_1 and match_object_2 and match_object_3 and match_object_4:
        return True
    else:
        return False


def main():
    doctest.testmod()
    print(password_validator('helG4'))


if __name__ == '__main__':
    main()
