def compound_interest(principal, annual_interest_rate, compounds_per_year, number_of_years):
    money_in_account = principal*((1+(annual_interest_rate/compounds_per_year))**(compounds_per_year*number_of_years))
    return money_in_account


def main():
    print(compound_interest(100, 0.10, 4, 10))


if __name__ == '__main__':
    main()

