def searchInsert( nums: int, target: int) -> int:
  pos = 0
  for i in range(len(nums)):
    if nums[i] < target:
      pos = i + 1
  return pos
print(searchInsert([1,2,3,7], 6))