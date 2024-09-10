# Calculate Sum of Digits
# Write a function called sum_of_digits that takes a positive integer as an argument and
# returns the sum of its digits.

def sum_of_digits(num: int):
  if num == 0:
    return 0
  sum = 0

  while num > 0:
    sum = sum + num % 10
    num = num // 10
  print(sum)
sum_of_digits(255250)