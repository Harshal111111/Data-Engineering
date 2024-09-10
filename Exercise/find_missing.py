def find_missing_number(nums):
  for i in range(0, len(nums)):
    if i not in nums:
      return i


print(find_missing_number([0, 1, 3]))


# second Approach:
def find_missing_number(lst):
  n = len(lst)  # Since n is one less than the length of the list
  expected_sum = n * (n + 1) // 2
  actual_sum = sum(lst)
  return expected_sum - actual_sum
