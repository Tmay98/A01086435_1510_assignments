
def colour_mixer():
    colour_1 = input("Enter the first primary colour to mix: ")
    colour_2 = input("Enter the second primary colour to mix: ")
    colour_1 = colour_1.strip()
    colour_2 = colour_2.strip()
    colour_1 = colour_1.lower()
    colour_2 = colour_2.lower()

    if ((colour_1 == 'blue' or colour_1 == 'yellow' or colour_1 == 'red')
            and (colour_1 == 'blue' or colour_1 == 'yellow' or colour_1 == 'red')):
        if (colour_1 == 'red' and colour_2 == 'blue') or (colour_1 == 'blue' and colour_2 == 'red'):
            print('purple')
        elif (colour_1 == 'red' and colour_2 == 'yellow') or (colour_1 == 'yellow' and colour_2 == 'red'):
            print('orange')
        elif (colour_1 == 'yellow' and colour_2 == 'blue') or (colour_1 == 'blue' and colour_2 == 'yellow'):
            print('green')
        else:
            print('you entered two of the same primary colour')
    else:
        print("You did not enter a primary colour")
    return


def main():
    colour_mixer()


if __name__ == '__main__':
    main()

