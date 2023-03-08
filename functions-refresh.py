#!/usr/bin/env python3

# def collection of instructions/code function
def function1():
    print('This is inside the fuction.')

# def mapping function 
def function2(x, y):
    return x + 7

def function3(x):
    print('The return value is different than the one printed.')
    print(x)
    return 10*x


# call the function

function1()
a = function2(3, 10)
print(a)

b = function3(5)
print('return value is: ', b)

