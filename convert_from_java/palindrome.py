#!/usr/bin/env python3

'''
Adapted from: Cheryl Moser - Week 4 Practice Exercise
I created three empty strings in the following static method: "backwards" simply creates 
 the word or phrase in reverse, exactly as it's typed; "input" is a version of the word 
 or phrase with spaces and punctuation removed; and "result" is the backward version of
 the word or phrase with spaces and punctuation removed.
'''

def Palindrome(word):
    backwards_alpha_only = ''           # result
    word_alpha_only = ''                # input
    backwards = ''                      # backwards

    for character in word:
        backwards = character + backwards
        if character.isalpha():
            word_alpha_only = word_alpha_only + character
    
    for character in word_alpha_only:
        backwards_alpha_only = character + backwards_alpha_only

    if word_alpha_only.lower() == backwards_alpha_only.lower():
        print(f'{word} printed backwards is {backwards} '
              'Ignoring spaces and punctuation, this word or phrase is a palindrome '
              f'In other words, {word_alpha_only} equals {backwards_alpha_only} '
        )
    else:
        print(f'Not a palindrome')

    return backwards_alpha_only

Palindrome("Madam, I'm Adam")

Palindrome("Check me one two One two check.")

