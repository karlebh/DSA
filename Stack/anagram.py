# anagram: checking off

def anagram_1(string_1, string_2):
	stringTwoList = list(string_2)

	postion_1 = 0
	still_ok = True

	while postion_1 < len(string_1) and still_ok:
		postion_2 = 0
		found = False

		while postion_2 < len(stringTwoList) and not found:
			if string_1[postion_1] == stringTwoList[postion_2]:
				found = True
			else:
				postion_2 = postion_2 + 1
		if found:
			stringTwoList[postion_2] = None
			# still_ok = True
		else: 
			still_ok = False

		postion_1 = postion_1 + 1

	return still_ok
# O(n2)

print(anagram_1('caleb', 'belac'))


# Sort and Compare

def anagram_2(string_1, string_2):
	listOne = list(string_1)
	listTwo = list(string_2)

	listOne.sort()
	listTwo.sort()

	position = 0
	matches = True

	while position < len(string_1) and matches:

		if listOne[position] == listTwo[position]:
			position = position + 1
		else:
			matches = False

	return matches
# n + (n2 or n log n)
print(anagram_2('caleb', 'belac'))

# Brute Force

# Error: will take about 77 billion years


# Count and Compare

def anagram_3(string_1, string_2):
	counterOne = [0] * 26
	counterTwo = [0] * 26

	for i in range(len(string_1)):
		position = ord(string_1[i]) - ord('a')
		print(position)
		counterOne[position] = counterOne[position] + 1

	for i in range(len(string_2)):
		position = ord(string_2[i]) - ord('a')
		counterTwo[position] = counterTwo[position] + 1

	j = 0
	still_ok = True
	while j < 26 and still_ok:
		if counterOne[j] == counterTwo[j]:
			j = j + 1
		else:
			still_ok = False

	return still_ok

# O(n) But utilises a lot of spaces

print(anagram_3('caleb', 'belac'))
