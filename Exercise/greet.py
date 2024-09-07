
# Basic String Manipulation
# Write a function called greet that takes two arguments: name (a string) and age (an integer).
# The function should return a string message in the format "Hello, [name]! You are [age] years old."


def greet(name: str, age: int) -> str:
  print (f'Hello, {name}! You are {age} years old.')
n = input("Enter name:\n")
a = int(input("Enter age: \n"))

greet(n, a)