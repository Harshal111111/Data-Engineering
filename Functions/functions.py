from orca.punctuation_settings import square_root
from pyatspi import interface

a = int(input("enter any number: \n"))
def squared(x: int):
    y = x**2
    return y

def cube(x: int):
    y = x**3
    return y
def sqr_root(x: int):
    y = x ** 0.5
    return int(y)
def cube_root(x: int):
    y =  x ** (1/3)
    return int(y)

def table(x: int):
    print(f' The table of {x} is :')
    for i in range(1,11):
        print (f'{x} x {i} = {x*i}')

def type_of(x: int):
    if x % 2 == 0:
        print(f'{x} is even number')
    else:
        print(f'{x} is odd ')

def factorial(x: int):
    fact = 1
    for i in range(1, x+1):
        fact *= i
    return(fact)




print (f'The square of {a} is {squared(a)}')
print (f'The cube of {a} is {cube(a)}')
print(f'The Square root of {a} is {sqr_root(a)}')
print(f'The Cube root of {a} is {cube_root(a)} ')
print (f'The factorial of {a} is {factorial(a)} ')
type_of(a)
table(a)

