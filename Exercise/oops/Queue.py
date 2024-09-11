# Implement a Queue
# Create a class called Queue that implements a queue data structure.
# The queue should support the following operations:
# enqueue(item): Adds an item to the back of the queue.
# dequeue(): Removes and returns the item from the front of the queue.
# peek(): Returns the item at the front of the queue without removing it.
# is_empty(): Returns True if the queue is empty and False otherwise.

class Queue:
  def __init__(self):
    self.queue = []
    # Initialize an empty queue
    pass

  def enqueue(self, item):
    self.queue.append(item)

    # Add the item to the back of the queue
    pass

  def dequeue(self):
    if not self.is_empty():
      return self.queue.pop(0)
    else:
      return None
    # Remove and return the item from the front of the queue
    pass

  def peek(self):
    if not self.is_empty():
      return self.queue[0]
    else:
      return None
    # Return the item at the front of the queue without removing it
    pass

  def is_empty(self):
    return len(self.queue) == 0
    # Return True if the queue is empty, False otherwise
    pass

  def size(self):
    if not self.is_empty():
      return len(self.queue)
    else:
      return 0
    # Return the number of items in the queue
    pass


queue = Queue()
queue.enqueue(1)
queue.enqueue(2)
queue.enqueue(3)

print(queue.dequeue())  # Should print 1
print(queue.peek())  # Should print 2
print(queue.is_empty())  # Should print False
print(queue.size())  # Should print 2
