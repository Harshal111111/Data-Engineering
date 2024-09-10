# Check for Prime Numbers
# Create a function called is_prime that takes an integer as input and returns True
# if the number is prime and False otherwise.
# >>> is_prime(5)
# True
# >>> is_prime(17)
# True
# >>> is_prime(4)
# False
# >>> is_prime(1)
# False

def check_prime(number):
  if number <=1:
    return False
  if number == 2:
    return True
  if number % 2 == 0:
    return False
  for i in range(2, number):
    if number % i == 0:
      return False
    else:
      return True

print(check_prime(7))
print(check_prime(17))
print(check_prime(7))
print(check_prime(10))
print(check_prime(2))
print(check_prime(5))