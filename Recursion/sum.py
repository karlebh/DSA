# def sum(numbers):
# 	sum = 0

# 	for i in numbers:
# 		sum = sum + i
# 	return sum

# print(sum([1,2,3,4]))

def sum(numbers):
	if len(numbers) == 1:
		return numbers[0]
	else:
		return numbers[0] + sum(numbers[1:])

print(sum([1,2,3,4]))
