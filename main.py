class Node:
  def __init__(self, value):
    self.value = value
    self.next = None


class Stack:
  def __init__(self):
    self.top = None
    self.botton = None
    self.length = 0

  def push(self, value):
    new_node = Node(value)
    if self.isEmpty:
      self.top = new_node
      self.botton = new_node
      self.length += 1
    else:
      holdingpointer = self.top
      self.top = new_node
      self.top.next = holdingpointer
      self.length += 1

    return self
  def pop(self):
    if self.top == None:
      return None

    holdingpointer = self.top
    self.top = holdingpointer.next
    self.length -= 1
    return holdingpointer.value

  def peek(self):
    return self.top

  @property
  def isEmpty(self):
    return self.length == 0

  @property
  def items(self):
    if self.isEmpty:
      return []
    values = []
    current_node = self.top
    while current_node != None:
      values.append(current_node.value)
      current_node = current_node.next
    return values


stack = Stack()

print(stack.peek())
stack.push('google')
print(stack.items)
stack.push('yahoo')
print(stack.items)
stack.push('gmail')
print(stack.items)
# print(stack.peek().value)

print(stack.pop())
print(stack.pop())
print(stack.pop())
print(stack.pop())
print(stack.isEmpty)
print(stack.items)
