# Count Occurrences in a List
# Write a Python function that takes a list of numbers and a target number,
# and it returns the count of how many times the target number appears in the list.
# In: ([1, 2, 3, 4, 2, 2, 5], 2)
# Out: 3

def count_occurrences(numbers, target):
  if len(numbers) == 0:
    return False
  if target not in numbers:
    return False
  if numbers.count(target) == 1:
    return 1
  if numbers.count(target) >= 2:
    return numbers.count(target)
num = []
tar = 2
print((count_occurrences(num, tar)))