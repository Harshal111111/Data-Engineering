def addBinary(a: str, b: str) -> str:
  result = []
  i, j = len(a) - 1, len(b) - 1
  carry = 0

  # Traverse both strings from the end
  while i >= 0 or j >= 0 or carry:
    # Get the current digits (or 0 if the index is out of bounds)
    digit_a = int(a[i]) if i >= 0 else 0
    digit_b = int(b[j]) if j >= 0 else 0

    # Calculate the sum of both digits and the carry
    total = digit_a + digit_b + carry

    # Append the result of current digit (total % 2 gives the bit)
    result.append(str(total % 2))

    # Calculate the new carry (total // 2 gives the carry)
    carry = total // 2

    # Move to the next digits
    i -= 1
    j -= 1

  # Since we added digits in reverse order, reverse the result list
  return ''.join(reversed(result))


# Example usage
print(addBinary("11", "1"))  # Output: "100"
print(addBinary("1010", "1011"))  # Output: "10101"
