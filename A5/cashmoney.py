"""cashmoney function"""

# Tommy May
# A01086435


def cashmoney(amount: float):
    breakdown_dict = {100: 0, 50: 0, 20: 0, 10: 0, 5: 0, 2: 0, 1: 0, 0.25: 0, 0.10: 0, 0.05: 0, 0.01: 0}
    for key in breakdown_dict.keys():
        breakdown_dict[key] = int(amount // key)
        amount = amount % key
    return breakdown_dict


def main():
    print(cashmoney(215.5))


if __name__ == "__main__":
    main()
