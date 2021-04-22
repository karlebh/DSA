def binary_search(list, item):

	first = 0
	last = len(list) - 1
	found = False

	while first <= last and not found:

		midpoint = (first + last) // 2

		if list[midpoint] == item:
			found = True
		else:
			if item < list[midpoint]:
				last = midpoint - 1
			else:
				first = midpoint + 1

	return found

print(binary_search([2,3,4,2,4,5,33,55,3,3], 40))


def binary_search_recursive(list, item):
	
	if len(list) == 0:
		return False
	else:
		midpoint = len(list) // 2

	if list[midpoint] == item:
		return True
	else:
		if item < list[midpoint]:
			return binary_search_recursive(list[:midpoint], item)
		else:
			return binary_search_recursive(list[midpoint + 1:], item)

print(binary_search_recursive([12,2,4,5,33,55,3,3], 4))

# O(log n) the only overhead is the sorting if an unordered list is given. In this case, it worse
# case might/shall/could/will be O(n)

