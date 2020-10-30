#!/usr/bin/python3

##
# what is input and output
# understand the data types
# understand how things are sorted/interfaced
##

import random

def guessNumber(guess, number):
     if guess != number:
        while True:
            guess = input("Guess again ")
        print('Yes! The number is ' + str(number))


def main():
    while True:
        msg = input("What should I do? ")
        if msg == "quit":
            break
        print(msg)

# create a list for numbers
numbers = []

#ask for inputs
numbers.append(int(input('Enter a number  ')))
numbers.append(int(input('Enter another number  ')))

# sort numbers to min, max
numbers.sort()

#create a random number between min, max
number = random.randrange(numbers[0], numbers[1])
print('number: ', number)

msg = 'guess a number between ' + str(numbers) + ' '
guess = int(input(msg))
print('guess: ', guess)

guessNumber(guess, number)


        