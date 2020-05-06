#!/usr/bin/env python3


# sum all items in a list
def sum_list(items):
    total = 0
    for i in items:
        total += i
    return total

# multiply all items in a list
def multiply_list(items):
    total = 1
    for i in items:
        total *= i
    return total

# return the largest number in a list
def return_largest(items):
    items.sort()
    return items[-1]

def return_smallest(items):
    smallest = items[0]
    for i in items:
        if smallest > i:
            smallest = i
        return smallest


numbers = [8, 17, 121, 65, 93, 44, 5, 20, 4, 1]

print('Sum of all numbers is: ', sum_list(numbers))
print('All numbers multiplied is: ', multiply_list(numbers))
print('Largest number is: ', return_largest(numbers))
print('Smallest number is: ', return_smallest(numbers))