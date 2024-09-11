# Find the Maximum Class Edition
# Similarly to the previous exercise, find the maximum number of a list. This time, use a class instead. When initializing
# MaxNumberFinder you will need to provide nums as an argument
# finder = MaxNumberFinder([1,3,4,2])
# finder.find_max_number() #output 4


class MaxNumberFinder:
  def __init__(self, nums):
    self.nums = nums

  def find_max_number(self):
    if not self.nums:
      return None
    max_num = self.nums[0]

    for i in self.nums[1:]:
      if i > max_num:
        max_num = i

    return max_num


finder = MaxNumberFinder([1, 3, 4, 2])
print(finder.find_max_number())  # Output: 4

finder2 = MaxNumberFinder([-5, -1, -3, -4])
print(finder2.find_max_number())  # Output: -1
