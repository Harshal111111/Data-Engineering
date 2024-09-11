# Find the Longest Consecutive Subsequence
# Create a function called longest_consecutive_subsequence that takes a list of integers as input and returns the length of
# the longest consecutive subsequence of integers in the list. A consecutive subsequence is a sequence of integers where each
# integer appears exactly once and they are in consecutive order.

def longest_consecutive_subsequence(nums):
  if not nums:
    return 0

  nums = set(nums)
  longest_streak = 0
  for num in nums:
    if num - 1 not in nums:
      current_num = num
      current_streak = 1
      while current_num + 1 in nums:
        current_num += 1
        current_streak += 1
      longest_streak = max(longest_streak, current_streak)
  return longest_streak


nums = [100, 4, 200, 1, 3, 2]
result = longest_consecutive_subsequence(nums)
print(result)  # Output: 4 (the sequence is [1, 2, 3, 4])
