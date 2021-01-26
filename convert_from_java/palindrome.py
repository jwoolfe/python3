#!/usr/bin/env python3

'''
Adapted from: Cheryl Moser - Week 4 Practice Exercise
I created three empty strings in the following static method: "backwards" simply creates 
 the word or phrase in reverse, exactly as it's typed; "input" is a version of the word 
 or phrase with spaces and punctuation removed; and "result" is the backward version of
 the word or phrase with spaces and punctuation removed.
'''

# main
def main():
    while True:
        if check_word():
            break

# Get a word as input
def check_word():
    word = input('Enter a word or phrase: ')
    return Palendromeda(word)

# This is the way using any language
def Palindrome(word):
    backwards_alpha_only = ''           # result
    word_alpha_only = ''                # input
    backwards = ''                      # backwards

    for character in word.lower():
        backwards = character + backwards
        if character.isalpha():
            word_alpha_only = word_alpha_only + character
            backwards_alpha_only = character + backwards_alpha_only

    if word_alpha_only == backwards_alpha_only:
        print(f'{word} printed backwards is {backwards} '
              'Ignoring spaces and punctuation, this word or phrase is a palindrome '
              f'In other words, {word_alpha_only} equals {backwards_alpha_only} '
        )
    else:
        print(f'Not a palindrome')

    return backwards_alpha_only

# this is a more pythonic way
def Palendromeda(word):
    alpha_only = [letter for letter in word.lower() if letter.isalpha()]
    alpha_only = ''.join(alpha_only)
    backwards = alpha_only[::-1]
    if alpha_only == backwards:
        print(f'{word} printed backwards is {word[::-1]}')
        print('Good Job!')
        return True
    else:
        print(f'{word} is not a palindrome.')
        return False


#Palindrome("Madam, I'm Adam")
#Palendromeda("Don't nod")
#
#Palindrome("Check me one two One two check.")
#Palendromeda("A far-away planet in your mind.")


if __name__ == '__main__':
    main()


