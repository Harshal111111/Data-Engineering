# Even or Odd
# Write a function called is_even that takes a number as an argument and returns
# True if it's even, and False otherwise


def is_even(num):
  if int(num) > 0 and num % 2 == 0:
    return True
  else:
    return False

number = int(input("Enter a Number: \n"))
print(is_even(number))