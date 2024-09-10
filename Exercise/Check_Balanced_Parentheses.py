# Create a function called is_balanced_parentheses that takes a string containing only parentheses, brackets, and curly
# braces as input and returns True if the parentheses are balanced and False otherwise. The parentheses are considered
# balanced if they are closed in the correct order. Your function should use only built-in Python tools.
#
# >>> is_balanced_parentheses("()")
# True
# >>> is_balanced_parentheses("()[]{}")
# True
# >>> is_balanced_parentheses("(]")
# False
# >>> is_balanced_parentheses("([)]")
# False
# >>> is_balanced_parentheses("{[]}")
# True

def is_balanced_parentheses(s):
  stack = []
  mapping = {')': '(', ']': '[', '}': '{'}
  for char in s:
    if char in mapping:
      top_element = stack.pop() if stack else '#'
      if mapping[char] != top_element:
        return False
    else:
      stack.append(char)
  return not stack


print(is_balanced_parentheses("(){}[]"))