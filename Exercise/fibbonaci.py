# Fibonacci Series
# Write a program that generates the Fibonacci series up to a given number 'n'.
# fibonacci(0) -> []
# fibonacci(10) -> [0, 1, 1, 2, 3, 5, 8]
# fibonacci(23) -> [0, 1, 1, 2, 3, 5, 8, 13, 21]

def fibonacci(n):
  if n <= 0:
    return []
  fib_series = [0,1]
  while True:
    next_num = fib_series[-1] + fib_series[-2]
    if next_num > n:
      break
    fib_series.append(next_num)
  return fib_series
print(fibonacci(0))   # Output: []
print(fibonacci(10))  # Output: [0, 1, 1, 2, 3, 5, 8]
print(fibonacci(23))