# Calculate Average
# Write a Python program that calculates the average of a list of numbers.
#
# In:  [5, 10, 15, 20]
#
# Out:  12.5
#
# If the list is empty, return 0

def calculate_average(numbers):
  sum = 0
  if len(numbers) == 0:
    return 0
  for i in numbers:
    sum = sum + i
  average = sum / len(numbers)
  return average

print(calculate_average([5, 10, 15, 20]))