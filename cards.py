#!/usr/bin/env python3

###########################
## Create a deck of cards
## choose a random cards
## hint: import random
##########################

import random
from collections import namedtuple

deck = {}
suits = ['Diamonds', 'Hearts', 'Spades', 'Clubs']
face_cards = ['Jack', 'Queen', 'King', 'Ace']
cards = list(range(2, 11))
cards.extend(face_cards)

for suit in suits:
    deck[suit] = cards


suit_pick = random.choice(suits)
value_pick = random.choice(cards) 

print(f'{value_pick} of {suit_pick}')










