"""Base conversion function"""

# Tommy May
# A01086435


def base_conversion(base_from, number: int, base_to):
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
    print(base_conversion(10, 256, 2))


if __name__ == '__main__':
    main()



