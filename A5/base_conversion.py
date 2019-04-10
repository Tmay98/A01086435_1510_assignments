"""Base conversion function"""

# Tommy May
# A01086435


def base_conversion(base_from, number: int, base_to):
    converted_number = 0
    digits_list = [int(digit) for digit in str(number)]

    # convert number to base 10
    for i in range(len(digits_list)):
        converted_number += digits_list[len(digits_list) - 1 - i] * base_from ** i


def main():
    base_conversion(5, 43, 10)


if __name__ == '__main__':
    main()



