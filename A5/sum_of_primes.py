"""Function that returns sum of primes up to given number"""

# Tommy May
# A01086435

import math


def sum_of_primes(number):
    primes = []
    sum = 0

    for i in range(number+1):
        primes.append(True)
    primes[0] = False
    primes[1] = False

    for i in range(2, math.floor(math.sqrt(number))+1):
        for j in range(2, i):
            if i % j == 0:
                primes[i] = False
        temp = i * 2
        while temp <= number:
            primes[temp] = False
            temp += i

    for i in range(len(primes)):
        sum += i if primes[i] is True else 0
    return sum


def main():
    print(sum_of_primes(9))


if __name__ == '__main__':
    main()
