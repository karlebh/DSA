from Deque import Deque

def is_palindrome(word):	
	deque = Deque()

	for char in word:
		deque.add_rear(char)

	still_equal = True

	while deque.size() > 1 and still_equal:
		first = deque.remove_front()
		last = deque.remove_rear()

		if first != last:
			still_equal = False

		return still_equal

print(is_palindrome('worddrow'))
