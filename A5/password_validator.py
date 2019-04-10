"""Password validator function"""

# Tommy May
# A01086435

import re


def password_validator(password):

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
    print(password_validator('helG4'))


if __name__ == '__main__':
    main()
