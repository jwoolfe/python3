#!/usr/bin/env python3

## Exploring Object Oriented Programming

class PlayerCharacter:              # Class
    membership = True               # Class Object attribute (static)

    def __init__(self, name, age):
        if (self.membership):
            self.name = name        # Class attribute (dynamic)
            self.age = age          # Class attribute (dynamic)

    def shout(self):                # method
        print(f'My name is {self.name.upper()}')
        return 'done'

    def run(self):                  # method
        print(f'{self.name} runs to the other side of the room.')
        return 'done'


player1 = PlayerCharacter('Billy', 25)
player2 = PlayerCharacter('Cindy', 18)
player2.attack = 50

print(player1.shout())
print(player2.run())
print(player2.attack)
print(player2.membership)


## Exercise 1
#Given the below class:
class Cat:
    species = 'mammal'
    def __init__(self, name, age):
        self.name = name
        self.age = age


# 1 Instantiate the Cat object with 3 cats
cat1 = Cat('Willow', 21)
cat2 = Cat('Lenny', 6)
cat3 = Cat('Murray', 4)


# 2 Create a function that finds the oldest cat
def oldest(*argv):
        old = max(*argv)
        return old


# 3 Print out: "The oldest cat is x years old.". x will be the oldest cat age by using the function in #2
eldest = oldest(cat1.age, cat2.age, cat3.age)
print(f'The oldest cat is {eldest} years old.')
