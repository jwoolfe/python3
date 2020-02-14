#! /usr/bin/env python3

list_of_nums = range(1,51)

for num in list_of_nums:
    if num % 3 == 0 and num % 5 == 0:
        print(num, ": fizz buzz")
    elif num % 3 == 0:
        print(num, ": fizz")    
    elif num % 5 == 0:
        print(num, ": buzz")
    else:
        print(num, ":")
