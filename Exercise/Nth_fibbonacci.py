# Find the Nth Fibonacci Number
# Create a function called find_fibonacci that takes a non-negative integer n as input and returns the n-th Fibonacci number. The Fibonacci sequence is a series of numbers where each number is the sum of the two preceding ones, usually starting with 0 and 1. Your function should use only built-in Python tools.
#
# >>> find_fibonacci(0)
# 0
# >>> find_fibonacci(1)
# 1
# >>> find_fibonacci(5)
# 5
# >>> find_fibonacci(10)
# 55

def find_fibonacci(n):
  if n < 0:
    raise ValueError("The Value must be positive!!")


  if n == 0:
    return 0
  elif n == 1:
    return 1
  a,b = 0,1
  for i in range(2, n+1):
    a,b = b, a+b
  return  b
# print(find_fibonacci(-5))
print(find_fibonacci(0))
print(find_fibonacci(1))
print(find_fibonacci(5))
print(find_fibonacci(10))