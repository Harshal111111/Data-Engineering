
# Find Unique Elements
# Find the number of unique elements of a list: In: [1,3,4,5,6,7] Out: 6
# In: [1,1,3,4,5,5,6,7] Out: 6 (1 and 5 are duplicated and should be counted once)

def find_unique_elements(lst):
  lst2 = []
  for i in lst:
    if i not in lst2:
      lst2.append(i)
  print(len(lst2))

find_unique_elements([1, 1, 3, 4, 5, 5, 6, 7])