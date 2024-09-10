# Count Primes
# Description: Write a function that takes an integer n as input and returns the count of prime numbers less than n.
# Input: 10 Output: 4 (Primes less than 10: 2, 3, 5, 7)


def is_prime(num):
  if num <= 1:
    return False
  if num == 2:
    return True
  if num % 2 == 0:
    return False
  for i in range(3, int(num ** 0.5) + 1, 2):
    if num % i == 0:
      return False
  return True

def count_primes(n):
  count = 0
  for i in range(2, n):
    if is_prime(i):
      count += 1
  return count


# Test cases
print(count_primes(10))  # Output: 4 (Primes less than 10: 2, 3, 5, 7)
print(count_primes(20))  # Output: 8 (Primes less than 20: 2, 3, 5, 7, 11, 13, 17, 19)
print(count_primes(1))  # Output: 0 (No primes less than 1)