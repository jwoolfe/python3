#!/usr/bin/env python3

from datetime import date


print('\n** Sum all items in a list \n')
items = [4, 3, 2, 1, 22, 7]

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


print('\n\n** Function that calculates the collatz sequence ')
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


print('\n** Print twinkel twinkle little star.')
msg = 'Twinkle, twinkle, little star, \n'
msg += '\t How I wonder what you are! \n'
msg += '\t\t Up above the world so high, \n '
msg += '\t\t Like a diamond in the sky.\n'
msg += 'Twinkle, twinkle, little star,\n'
msg += '\t How I wonder what you are\n'
print(msg)

print('\n** Print python version ')
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

print('\n** Error handling ')
print(div42by(0))
print(div42by(1))


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

print('\n** Looking at lists with range ')
supplies = ['pens', 'staplers', 'binders', 'flask']
def indexes(listinput):
   for i in range(len(listinput)):
      print('Index ' + str(i) + ' in  listinput: ' + listinput[i])

indexes(supplies)

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
#print(f'Your password {hidden_pass} is {len(password)} letters long.')#
# print('\n\n')

print('\n** More List Methods with a fruit basket')

basket = ['Bananas', 'Apples', 'Oranges', 'Blueberries']

#1. remove Bananas
basket.remove('Bananas')

#2. Remove Blueberries
basket.pop()

#3. Add 'Kiwi' to the end
basket.append('Kiwi')

#4. Add Apples at the beginning
basket.insert(0, 'Apples')

#5. Count how many Apples in the basket
apple_count = basket.count('Apples')
print(f'There are {apple_count} apples in the basket.')

#6. Empty the basket
#basket.clear()

print('\n** Sorted list of friends')
friends = ['Simon', 'Patty', 'Joy', 'Carrie', 'Amira', 'Chu']
new_friend = ['Stanley']

friends.extend(new_friend)
print(sorted(friends))

print('\n\n** List unpacking ')
a,b,c, *other, d = [1,2,3,4,5,6,7,8,9]

print(a)
print(b)
print(other[3])
print(d)

print('\n\n** Dictionaries ')

# dictionary for users in game

user1 = {
    'username': 'Bono',
    'age': 20,
    'weapons': ['sword'],
    'is_active': True,
    'clan': 'Lumsden'
}

user1['weapons'].append('knife')
user1.update({'is_banned': True})

user2 = user1.copy()
user2.update({'username': 'Dono', 'age': 25})

print(user1)
print(user2.values())


print('\n\n** Sets ')
# unordererd collection of unique objects

school = {'Bobby', 'Tammy', 'Jammy', 'Sally', 'Danny'}
attendance_list = ['Bobby', 'Jammy', 'Sally', 'Danny']

print(f'{school.difference(attendance_list)} skipped class today.')

print('\n\n** Ternary Operator (Conditional Expression)')

# condition_if_true if condition else condition_if_false
is_friend = True
can_message = 'message allowed' if is_friend else 'not allowed to message'

print(can_message)

print('\n\n** Short Circuiting')
is_Friend = True
is_User = True

if is_Friend or is_User:
    print('BFFs! ')

print('\n\n** Logical Operators')

is_magician = False
is_expert = False

# check if magician AND expert
if is_magician and is_expert:
    print('You are a master magician')

# check if magician but not expert
elif is_magician and not is_expert:
    print('Your journey has begun')

# check if you're not a magician
elif not is_magician:
    print('Seek the powers of magic')


print('\n\n** Loop through dictionaries ')

# iterable - list, dictionary, tuple, set, string
# any collection of items can be iterated
# iterate - one by one, check each item in the collection
# for item in <data structure>:

# for dictionaries, the keys will be iterated
user = {
    'name': 'Golem',
    'age': 5006,
    'can_swim': False
}

# methods for iterating dictionaries
for item in user.items():
    print(item)

for item in user.values():
    print(item)

for item in user.keys():
    print(item)

for key, value in user.items():
    print(key, value)

print('\n\n** Loop through list ')
my_list = [1,2,3,4,5,6,7,8,9,10]

total = 0
for num in my_list:
    total = total + num
print(total)

print('\n** Loop Tools ')
# common looping tools -- range, enumerate
for number in range(0, 30, 3):  # step over 3 or use -1 for reverse
        print(number)

for i,char in enumerate('abc'):       # give us an index for each item
    print(i, char)

for i,char in enumerate(list(range(100))):
    if char == 50:
        print(i)


print('\n** While Loops, break, continue, pass ')

# To jump out of a while loop:
    # turn condition False (ex: with a counter or else)
    # break


# Python3 code to iterate over a list
list = [1, 2, 3, 4, 5]

# Iterating using the for loop
print('Iterating using for loop ')
newlist = []
for i in list:
    newlist.append(i)
print(newlist)
  
# Getting length of list
length = len(list)
i = 0

# Iterating using while loop
print('Iterating using while loop ')

while i < length:
    print(list[i])
    i += 1



# Very useful to use with input()
#While True:
#    response = input('say something: ')
#    if (response = 'bye'):
#        break

print('\n** Exercise: Make your first GUI')

picture = [
 [0,0,0,1,0,0,0],
 [0,0,1,1,1,0,0],
 [0,1,1,1,1,1,0],
 [1,1,1,1,1,1,1],
 [0,0,0,1,0,0,0],
 [0,0,0,1,0,0,0],
]


# way #1
graphic = []

for line in picture:
    graphicline = []
    for item in line:
        if item == 0:
            graphicline.append(' ')
        else:
            graphicline.append('*')
    graphic.append(graphicline)

# oops forgot the print part

# way #2
for row in picture:
    for pixel in row:
        if (pixel ==1):
            print('*', end='')
        else:
            print(' ', end='')
    print('')


print('\n** Exercise: Check for duplicates in a list')

some_list = ['a', 'b', 'c', 'b', 'd', 'm', 'n', 'n']
#count_dict = dict.fromkeys(some_list, 1)
some_dict = {}

# for each item in some_list, check if in count_dict
# if item exists as key, value=+1

for key in some_list:
    if key in some_dict.keys():
       # print(f' Element {key} exists in dict')
        some_dict[key] += 1
    else:
       # print(f' Adding {key} to dict')
        some_dict[key] = 1

dups = []
for key, value in some_dict.items():
    if value > 1:
        dups.append(key)

print('Way of the Jen: ', end = '')
print(dups) 

# way #2
some_list = ['a', 'b', 'c', 'b', 'd', 'm', 'n', 'n']

duplicates = []
for value in some_list:
    if some_list.count(value) > 1:
        if value not in duplicates:
            duplicates.append(value)

print(f'Way of the python warrior: {duplicates}')


print('\n** Exercise: ')







print('\n\n**** ')  # end
