#!/usr/bin/python3

from datetime import date
from calendar import monthrange

def main():

    # ask for user's name
    name = input('What is your name? ')
    print(f'Hi {name}!')

    # ask for user's birthmonth
    raw_bmonth = 'not a number'
    while not ismonth(raw_bmonth):
        raw_bmonth = input('What month is your birthday? (1-12) ')
    print(raw_bmonth)
    bmonth = int(raw_bmonth)

    raw_bday = 'not a number'
    while not isday(bmonth, raw_bday):
        raw_bday = input('What day is your birthday? (1-31) ')
    print(raw_bday)
    bday = int(raw_bday)

    past_or_future = past_or_future_month(bmonth)
    if past_or_future == 'now':
        past_or_future = past_or_future_day(bday)
    print(past_or_future)

def ismonth(month):
    if not month.isdigit():
        return False
    if int(month) > 13:
        return False
    if int(month) < 1:
        return False
    return True

def isday(month, day):
    year = date.today().year
    if not day.isdigit():
        return False
    if int(day) < 1:
        return False
    totaldays = monthrange(year, month)[1]
    if month == 2:
        totaldays = 29
    if int(day) > totaldays:
        return False
    return True


# Check if bday is in the past or future
def past_or_future_month(month):
    # Check today's date
    today = date.today().month
    if month < today:
        # already happened
        return 'past'
    if month > today:
        # not happened yet
        return 'future'
    return 'now' 

def past_or_future_day(day):
    today = date.today().day
    if day < today:
        # already happened
        return 'past'
    if day > today:
        # not happened yet
        return 'future'
    return 'now'



    # "Your birthday was x days ago."
    # "Your birthday is in x days from now"
    # "Happy Birthday!"


if __name__ == "__main__":
    main()