# Merge Sorted Lists
# Create a function called merge_sorted_lists that takes two sorted lists of integers as input and returns a single sorted list
# containing all the elements from both input lists.

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


# class ListNode:
#   def __init__(self, val=0, next=None):
#     self.val = val
#     self.next = next
#
#
# class Solution:
#   def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
#     # Create a dummy node to act as the head of the new merged list
#     dummy = ListNode()
#     current = dummy
#
#     # Traverse both lists until one of them is exhausted
#     while list1 and list2:
#       if list1.val < list2.val:
#         current.next = list1  # Attach the smaller node to the merged list
#         list1 = list1.next  # Move the pointer forward in list1
#       else:
#         current.next = list2  # Attach the smaller node to the merged list
#         list2 = list2.next  # Move the pointer forward in list2
#       current = current.next  # Move the current pointer in the merged list
#
#     # If any elements remain in either list, attach them to the merged list
#     if list1:
#       current.next = list1
#     elif list2:
#       current.next = list2
#
#     # Return the merged list, starting at the node after the dummy
#     return dummy.next
