#!/usr/bin/env python3

from datetime import date

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


def div42by(divideBy):
   try:
      return 42 / divideBy
   except ZeroDivisionError:
      print('Error: You tried to divide by zero')

# error handling
print(div42by(0))
print(div42by(1))

print('\n')
print('\n')


## error handling input
#numCats = input('How many cats do you have? ')
#try:
#   if int(numCats) >= 4:
#      print('That is a lot of cats')
#   else:
#      print('That is not that many cats')
#except ValueError:
#   print('You did not enter a number')
#print('\n\n')

## looking at lists with range
supplies = ['pens', 'staplers', 'binders', 'flask']
def indexes(listinput):
   for i in range(len(listinput)):
      print('Index ' + str(i) + ' in  listinput: ' + listinput[i])

indexes(supplies)

print('\n\n')

## inputs
#name = input('What is your name? ')
#birth_year = input('What year were you born? ')
#password = input('Please type in a password. ')
#
# calculations
#age = date.today().year - int(birth_year)
#hidden_pass = '*' * len(password)
#
## outputs
#print(f'{name}, you are {age} years old')
#print(f'Your password {hidden_pass} is {len(password)} letters long.')

print('\n\n')

# More Lists





print('\n\n')




