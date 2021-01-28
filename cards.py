#!/usr/bin/env python3

###########################
## dictionary for users 
## dictionary keys = usernames
## dict value = hand
##
##
## shuffle deck
## pop 5 cards for each player 
## print out what hands are
## extra credit: implement first unique character in a word (from memory)
##########################

import random
from collections import namedtuple

Card = namedtuple('Card', ['suit', 'value'])

suits = ['Diamonds', 'Hearts', 'Spades', 'Clubs']
face_cards = ['Jack', 'Queen', 'King', 'Ace']
values = list(range(2, 11))
values.extend(face_cards)

new_deck = []

for suit in suits:
    for value in values:
        card = Card(suit, value)
        new_deck.append(card)

random.shuffle(new_deck)
pick = new_deck.pop()


#print(f'You picked {pick[1]} of {pick[0]}')
print(f'{pick.value} of {pick.suit}')











