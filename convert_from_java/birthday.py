#!/usr/bin/python3

from datetime import date

def main():

    # ask for user's name
    name = input('What is your name? ')
    print(f'Hi {name}!')

    # ask for user's birthmonth
    raw_bmonth = input('What month is your birthday? (1-12) ') 

    if not raw_bmonth.isdigit():
        while True:
            raw_bmonth = input('Not a number. Please enter a number. ')
            print(f'Yes, {raw_bmonth} is a number.' )
            return
        print(f'{raw_bmonth} is not a number. Please enter a number. ')


    while True:
        bmonth = int(raw_bmonth)
        if (bmonth > 13):
            raw_bmonth = input('Too high. Please enter a number between 1-12 ')

    # ask for user's 







if __name__ == "__main__":
    main()