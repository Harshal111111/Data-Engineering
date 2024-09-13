#
# Reverse a String
# Create a function called reverse_string that takes a string as input and returns a
# new string with its characters reversed.

def reverse_string(input_string):
  reversed_string = ""
  for char in input_string:
    reversed_string = char + reversed_string
  return reversed_string


result = reverse_string("hello")
print(result)

