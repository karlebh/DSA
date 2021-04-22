from Stack import Stack

def balanced_parentheses(parentheses):

	stack = Stack()
	balanced = True
	index = 0

	while index < len(parentheses) and balanced:

		symbol = parentheses[index]

		if symbol == "(":
			stack.push(symbol)
		else:
			if stack.is_empty():
				balanced = False
			else:
				stack.pop()
		index = index + 1

	if balanced and stack.is_empty():
		return True
	else:
		return False

# print(balanced_parentheses("((())"))

def complex_balanced_parentheses(parentheses):

	stack = Stack()
	balanced = True
	index = 0

	while index < len(parentheses) and balanced:
		
		symbol = parentheses[index]
		if symbol in "{([":
			stack.push(symbol)
		else:
			if stack.is_empty():
				balanced = True
			else:
				top = stack.pop()
				if not matches(top, symbol):
					balanced = False
		index = index + 1
	if balanced and stack.is_empty():
		return True
	else:
		return False

def matches(open, close):
	opens = "({["
	closes = ")}]"
	return opens.index(open) == closes.index(close)

print(complex_balanced_parentheses("([{}{}])"))
	
