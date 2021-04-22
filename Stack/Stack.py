class Stack:

	def __init__(self):
		self.items = []

	def is_empty(self):
		return self.items == []

	def push(self, item):
		self.items.append(item)

	def pop(self):
		return self.items.pop()

	def peek(self):
		return self.items[len(self.items) - 1]

	def size(self):
		return len(self.items)

	# def delete(self, item):
	# 	self.items.pop(item)

# stack = Stack()
# stack.is_empty()
# stack.push('Hello')
# stack.push('World')
# stack.pop()
# stack.peek()
# stack.size()
# stack.is_empty()
