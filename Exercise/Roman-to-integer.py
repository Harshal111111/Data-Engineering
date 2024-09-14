def roman_to_int(s):
  sum = 0
  n = len(s)
  mapping = {
    "I": 1,
    "V": 5,
    "X": 10,
    "L": 50,
    "C": 100,
    "D": 500,
    "M": 1000
  }
  for i in range(n):
    if i < n-1 and mapping[s[i]] < mapping[s[i+1]]:
      sum = sum - mapping[s[i]]
    else:
      sum = sum + mapping[s[i]]
  return sum
print(roman_to_int("MCMXCIV"))