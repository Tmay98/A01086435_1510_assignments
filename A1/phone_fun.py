def number_translator():
    phone_number = input("Enter a phone number in the format XXX-XXX-XXXX: ")
    converted_number = recursive_translator(phone_number, len(phone_number)-1)
    return converted_number


def recursive_translator(number_string, number_length):
    converted_string = ''
    string_index = 11 - number_length

    if string_index == 12:
        return ''

    if number_string[string_index] == 'A' or number_string[string_index] == 'B' or number_string[string_index] == 'C':
        converted_string = '2' + recursive_translator(number_string, number_length - 1)

    elif number_string[string_index] == 'D' or number_string[string_index] == 'E' or number_string[string_index] == 'F':
        converted_string = '3' + recursive_translator(number_string, number_length - 1)

    elif number_string[string_index] == 'G' or number_string[string_index] == 'H' or number_string[string_index] == 'I':
        converted_string = '4' + recursive_translator(number_string, number_length - 1)

    elif number_string[string_index] == 'J' or number_string[string_index] == 'K' or number_string[string_index] == 'L':
        converted_string = '5' + recursive_translator(number_string, number_length - 1)

    elif number_string[string_index] == 'M' or number_string[string_index] == 'N' or number_string[string_index] == 'O':
        converted_string = '6' + recursive_translator(number_string, number_length - 1)

    elif number_string[string_index] == 'P' or number_string[string_index] == 'Q' or number_string[string_index] == 'R' or number_string[string_index] == 'S':
        converted_string = '7' + recursive_translator(number_string, number_length - 1)

    elif number_string[string_index] == 'T' or number_string[string_index] == 'U' or number_string[string_index] == 'V':
        converted_string = '8' + recursive_translator(number_string, number_length - 1)

    elif number_string[string_index] == 'W' or number_string[string_index] == 'X' or number_string[string_index] == 'Y' or number_string[string_index] == 'Z':
        converted_string = '9' + recursive_translator(number_string, number_length - 1)

    else:
        converted_string = number_string[string_index] + recursive_translator(number_string, number_length - 1)

    return converted_string


def main():
    print(number_translator())


if __name__ == '__main__':
    main()
