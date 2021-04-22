
def Sequential(list, item):

	position = 0
	found = False

	while position < len(list) and not found:
		if list[position] == item:
			found = True
		else:
			position = position + 1

	return found

# print(Sequential([1,2,3,4,5,6,7,8,9,0], 99))

def Sequential_Ordered(list, item):

	position = 0
	found = False
	stop = False

	while position < len(list) and not found and not stop:
		if list[position] == item:
			found = True
		elif list[position] > item:
			stop = True
		else:
			position = position + 1

	return found


print(Sequential_Ordered([1,2,3,5,6,7,8,9,0], 3))


	
