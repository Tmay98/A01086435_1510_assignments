"""gcd calculator function"""

# Tommy May
# A01086435

from math import floor


def gcd(a: int, b: int):
    if a == 0:
        return b
    elif b == 0:
        return a
    else:
        return gcd(b, a - b * floor(a / b))


def main():
    print(gcd(-25, 15))


if __name__ == '__main__':
    main()
