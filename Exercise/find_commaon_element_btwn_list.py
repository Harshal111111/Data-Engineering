# Find Common Elements in Two Lists
# Create a function called find_common_elements that takes two lists of integers as input and returns a list
# containing the common elements between the two input lists. The order of elements in the resulting list does not matter.
# >>> find_common_elements([1, 2, 3, 4, 5], [3, 4, 5, 6, 7])
# [3, 4, 5]
# >>> find_common_elements([10, 20, 30], [30, 40, 50])
# [30]
# >>> find_common_elements([1, 2, 3], [4, 5, 6])
# []
# >>> find_common_elements([], [1, 2, 3])
# []

def find_common_elements(list1, list2):
  return list(set(list1) & set(list2))


print(find_common_elements([1, 2, 3, 4, 5], [3, 4, 5, 6, 7]))
