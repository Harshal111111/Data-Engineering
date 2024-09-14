# Write a function called is_palindrome that takes a string as a
# n argument and returns True if it('s a palindrome, and False otherwise. '
# 'A palindrome is a word, number, phrase, or other sequence of symbols that reads
# the same backward as forward                                                                                      'forwards, such as madam or racecar.)

def is_palindrome(s):
  s = s.replace(" ", "").lower()
  return s == s[::-1]


print(is_palindrome("madam"))         # Output: True
print(is_palindrome("racecar"))       # Output: True
print(is_palindrome("hello"))         # Output: False
print(is_palindrome("A man a plan a canal Panama"))  # Output: True


# For Digit:
class Solution:
  def isPalindrome(self, x: int) -> bool:
    rev = 0
    num = x
    while x > 0:
      digit = x % 10
      rev = rev * 10 + digit
      x = x // 10
    return num == rev
