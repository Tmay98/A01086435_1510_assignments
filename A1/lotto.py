import random


def number_generator():
    lottery_numbers = random.sample(range(50), 6)
    lottery_numbers.sort()
    return lottery_numbers


def main():
    print(number_generator())


if __name__ == '__main__':
    main()







