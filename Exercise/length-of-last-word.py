def lengthOfLastWord(s: str) -> int:
  words = s.split()
  return (len(words[-1]))
print(lengthOfLastWord("hello world"))