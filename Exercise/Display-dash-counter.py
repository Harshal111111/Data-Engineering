# You are given a string, which consists of decimal digits (0-9).
# Each digit is made of a certain number of dashes, as shown in the image below.
# For instance, 1 is made of 2 dashes, 8 is made of 7 dashes and so on.
# In this seven-segment display the digits are created by, illuminating, following set of dashes:
# 1. 2        6. 6
# 2. 5        7. 4
# 3. 5        8. 7
# 4. 4        9. 6
# 5. 5        0. 6

def display_(strs):
  mapping = { "1": 2, "2": 5, "3": 5, "4": 4,"5" : 5, "6" : 6, "7": 4, "8": 7, "9": 6 , "0": 6}
  result = 0
  for i in strs:
    if i in mapping:
      result = result + mapping[i]
  return result
s = input("enter any number \n")
print(display_(s))