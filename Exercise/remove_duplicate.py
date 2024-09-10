
# Remove Duplicates from a List
# Create a function called remove_duplicates that takes a list of elements as input and returns a new list with
# duplicates removed. Your function should use only built-in Python tools and should maintain the original order of
# elements while removing duplicates.
#
# >>> remove_duplicates([1, 2, 2, 3, 4, 4, 5])
# [1, 2, 3, 4, 5]
# >>> remove_duplicates(['apple', 'banana', 'apple', 'cherry'])
# ['apple', 'banana', 'cherry']
# >>> remove_duplicates([1, 2, 3])
# [1, 2, 3]
# >>> remove_duplicates([])
# []

def remove_duplicates(input_list):
  test = []
  for i in input_list:
    if i not in test:
      test.append(i)
  return test


print(remove_duplicates([1, 2, 2, 3, 4, 4, 5]))