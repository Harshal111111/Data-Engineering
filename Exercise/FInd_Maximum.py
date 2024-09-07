# Find the Maximum
# Find the Maximum Number in a List Description:
# Write a function that takes a list of numbers as input and returns the maximum number in the list.
# Input: [5, 9, 2, 12, 7] Output: 12
# If the argument is empty or None return None:
# Input: []
# Output: None

def find_max_number(numbers):
    if len(numbers) == 0:
        return None
    else:
        max = 0
        for i in numbers:
            if i > max:
                max = i
        return max
num = []
print(find_max_number(num))