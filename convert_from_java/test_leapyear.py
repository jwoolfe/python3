# Use TDD to test leap year functions
##  Tests
# _x_ Can call LeapYear
# _x_ Returns false for not divisible by 4
# _x_ Returns true for divisible by 4 but not 100 or 400
# ___ Ret false for div by 4 but is div by 100 but not 400
# ___ Returns true for div by 4, div by 100, div by 400
#
##

import pytest

def leapYear(year):
    if year % 4 == 0:
        if year % 100 == 0:
            if year % 400 == 0:
                return True
            return False
        return True
    return False

def checkLeapYear(year, expected_result):
    ret_value = leapYear(year)
    assert ret_value == expected_result

def test_returnFalseNotDivisibleBy4():
    checkLeapYear(1995, False)

def test_returnTrueDivisibleBy4():
    checkLeapYear(1996, True)

def test_returnFalseDivisibleBy4And100():
    checkLeapYear(2100, False)

def test_returnTrueDivisibleBy4And400():
    checkLeapYear(2000, True)