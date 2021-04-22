from Stack import Stack

def number_to_binary(number):

	stack = Stack()

	while number > 0:
		remainder = number % 2
		stack.push(remainder)
		number = number // 2

	binary = ""
	while not stack.is_empty():
		binary = binary + str(stack.pop())

	return binary

print(number_to_binary(8))


def complex_number_to_binary(number, base):

	digits = "1234567890ABCDEF"
	stack = Stack()

	while number > 0:
		remainder = number % base
		stack.push(remainder)
		number = number // base

	binary = ""
	while not stack.is_empty():
		binary = binary + digits[stack.pop()]

	return binary

print(complex_number_to_binary(8, 9))


