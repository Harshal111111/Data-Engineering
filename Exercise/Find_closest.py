# Find The Closest Number
# Write a function that finds the first closest number in a list
# In: ([2, 4, 8, 10], 6)
# Out: 4

def find_closest(numbers, target):
  if len(numbers) == 0:
    return None
  closest = numbers[0]
  for num in numbers:
    if abs(num - target) < abs(target - closest):
      closest = num
  return closest

print(find_closest([2,4,8,10], 6))