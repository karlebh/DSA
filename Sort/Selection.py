def Selection(list):
	for i in range(len(list)):
		min_idx = i
		for j in range(i + 1, len(list)):
			if list[min_idx] > list[j]:
				min_idx = j
		list[i], list[min_idx] = list[min_idx], list[i]
	return list

print(Selection([1,4,2,6,3,80,9,4,5,3,222,1]))