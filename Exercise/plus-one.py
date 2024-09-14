def plus_one(digits):
  n = len(digits)

  # Start from the end of the digits array
  for i in range(n - 1, -1, -1):
    # Increment the current digit
    digits[i] += 1

    # If the current digit becomes 10, set it to 0 and carry 1 to the next digit
    if digits[i] == 10:
      digits[i] = 0
    else:
      # No carry needed, so return the result
      return digits

  # If we exit the loop, it means we need to handle the carry over for the most significant digit
  return [1] + digits


# Example usage
print(plus_one([1, 2, 3]))  # Output: [1, 2, 4]
print(plus_one([4, 3, 2, 1]))  # Output: [4, 3, 2, 2]
print(plus_one([9]))  # Output: [1, 0]
