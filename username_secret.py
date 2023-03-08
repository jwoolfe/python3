#!/usr/bin/env python3

import maskpass

username = input('What the fuck is your name? ')
secret = maskpass.askpass('What the fuck is your password? ')
length = len(secret)

hidden_secret = '*' * length

msg = ''
if length >= 6:
    msg = 'your password is really big!'
else:
    msg = 'your password is not what I expected.'

print(f'Jesus, {username}, {hidden_secret} is {length} characters long. Dayyumn, {msg}')

