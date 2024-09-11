# Create a class called Stack that implements a stack data structure. The stack should support the following operations:
#   1. push(item): Pushes an item onto the top of the stack.
#   2. pop(): Removes and returns the item at the top of the stack.
#   3. peek(): Returns the item at the top of the stack without removing it.
#   4. is_empty(): Returns True if the stack is empty and False otherwise.
#   5. size(): Returns the number of items in the stack.

class Stack:
  def __init__(self):
    self.stack = []
    pass

  def push(self, item):
    self.stack.append(item)
    # Push the item onto the stack
    pass

  def pop(self):
    if not self.is_empty():
      return self.stack.pop()
    else:
      return None
    # Remove and return the item at the top of the stack
    pass

  def peek(self):
    if not self.is_empty():
      return self.stack[-1]
    else:
      return None
    # Return the item at the top of the stack without removing it
    pass

  def is_empty(self):
    return len(self.stack) == 0
    # Return True if the stack is empty, False otherwise
    pass

  def size(self):
    if not self.is_empty():
      return len(self.stack)
    else:
      return 0
    # Return the number of items in the stack
    pass


stack = Stack()
stack.push(1)
stack.push(2)
stack.push(3)

print(stack.pop())  # Output: 3
print(stack.peek())  # Output: 2
print(stack.is_empty())  # Output: False
print(stack.size())  # Output: 2
