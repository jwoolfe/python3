#!/usr/bin/env python3

items = [4, 3, 2, 1, 22, 7]

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
# slow way
def return_largest(items):
    items = sorted(items)
    return items[-1]
# fast way
max(items)

# return the smallest item in a list
# slowest way
def return_smallest(items):
    items = sorted(items)
    return items[0]

# slow way
def return_smallest_faster(items):
    smallest = items[0]
    for i in items:
        if smallest > i:
            smallest = i
    return smallest

# fast way
min(items)


numbers = [8, 17, 121, 65, 93, 44, 5, 20, 4, 1 ]

print('Sum of all numbers is: ', sum_list(numbers))
print('All numbers multiplied is: ', multiply_list(numbers))
print('Largest number is: ', return_largest(numbers))
print('Smallest number is: ', return_smallest(numbers))


print('\n')
# Function that calculates the collatz sequence
print('Collatz sequence : ')
def collatz(num):
    num = int(num)
    # print(num)
    if num % 2 == 0:     # even
        calc = num // 2
    else:                   # odd
        calc = (3 * num) + 1
    print(calc)
    return calc

#number = input("Enter a number: ")
number = 3
number = collatz(int(number))
while number != 1:
    number = collatz(number)


print('\n')
# Count number of strings in a list that meet a set of requirements
#       * characters > 2
#       * first and last letter the same

strings = ['24', 'xyzzz', 'abbbbba', '1221', '0fiaslkdj0']
count = 0
for string in strings:
    if len(string) > 2 and string[0] == string[-1]:
        count += 1
print('Expected Result : ', count)

print('\n')
# Sort a list of tuples by last element of tuple
sample = [(2,5), (1,2), (4,4), (2,3), (2,1)]

def second_element(t):
    return t[-1]
final = sorted(sample, key=second_element)
print(final)


# print twinkel twinkle little star.
print('\n')
print('\n')
msg = 'Twinkle, twinkle, little star, \n'
msg += '\t How I wonder what you are! \n'
msg += '\t\t Up above the world so high, \n '
msg += '\t\t Like a diamond in the sky.\n'
msg += 'Twinkle, twinkle, little star,\n'
msg += '\t How I wonder what you are\n'
print(msg)

print('\n')
print('\n')

# print python version
import sys
print("Python Version")
print (sys.version)
print("Version info")
print(sys.version_info)

print('\n')
print('\n')