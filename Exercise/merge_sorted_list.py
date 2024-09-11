# Merge Sorted Lists
# Create a function called merge_sorted_lists that takes two sorted lists of integers as input and returns a single sorted list
# containing all the elements from both input lists.

# def merge_sorted_lists(list1, list2):
#     if len(list1) and len(list2) == 0:
#         return 0
#     sorted_list = list1 + list2
#     res = []
#     for i in sorted_list:
#         if i not in res:
#             res.append(i)
#         sorted_list = res
#     return sorted_list

# print(merge_sorted_lists([1, 3, 5], [2, 4, 6]))
#     # Your code here


def merge_sorted_lists(list1, list2):
  merged_list = []
  i, j = 0, 0

  # Merge elements from both lists in sorted order
  while i < len(list1) and j < len(list2):
    if list1[i] < list2[j]:
      merged_list.append(list1[i])
      i += 1
    else:
      merged_list.append(list2[j])
      j += 1

  # If there are remaining elements in list1 or list2, append them
  merged_list.extend(list1[i:])
  merged_list.extend(list2[j:])

  return merged_list

list1 = [1, 3, 5]
list2 = [2, 4, 6]
result = merge_sorted_lists(list1, list2)
print(result)  # Output: [1, 2, 3, 4, 5, 6]
