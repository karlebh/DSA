import DSA.Stack.Stack;

print(Stack)

# def Bubble(list):
# 	for num in range(0, len(list)):
# 		for i in range(0, len(list) - 1):
# 			if list[i] > list[i + 1]:
# 				# temp = list[i]
# 				# list[i] = list[i + 1]
# 				# list[i + 1] = temp
# 				list[i], list[i + 1] = list[i + 1], list[i]
# 	return list

# print(Bubble([2,1,4,3,5,6,0,5,8,3,2,9]))


# def Short_Bubble(list):
# 	exchanges = True
# 	num = len(list) - 1

# 	while num > 0 and exchanges:
# 		exchanges = False
# 		for i in range(num):
# 			if list[i] > list[i + 1]:
# 				exchanges = True
# 				temp = list[i]
# 				list[i] = list[i + 1]
# 				list[i + 1] = temp
# 		num = num + 1
# 		