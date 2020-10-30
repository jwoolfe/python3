#!/usr/bin/python3

number = 5

def guessNumber(guess, number):
        print('** number: ', number)
        print('** guess: ', guess)
        if guess != number:
            while True:
                guess = input("Guess again ")
          #  else:
        print('Yes! The number is ' + str(number))

def main():
    while True:
        msg = input("What should I do? ")
        if msg == "quit":
            break
        print(msg)


msg = 'guess a number between 1 and 10 '
guess = int(input(msg))
guessNumber(guess, number)