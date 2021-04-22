def binary_tree(root):
	return [root, [100, 123], []]

def insert_left(root, new_branch):
	t = root.pop(1)
	if len(t) > 1:
		root.insert(1, [new_branch, t, []])
	else:
		root.insert(1, [new_branch, [], []])
	return root

def insert_right(root, new_branch):
	t = root.pop(2)
	if len(t) > 1:
		root.insert(2, [new_branch, [], t])
	else:
		root.insert(2, [new_branch, [], []])
	return root

def get_root_value(root):
	root[0]

def set_root_value(root, value):
	root[0] = value

def get_left_child(root):
	return root[1]

def get_right_child(root):
	return root[2]

r = binary_tree(3)
insert_right(r, 5)
insert_left(r, 4)
# insert_right(r, 45)
# insert_left(r, 92)
print(r)

# l = get_left_child(r)
# print(r)

# set_root_value(l, 90)
# print(r)

# insert_left(l, 11)
# print(r)

# print(get_right_child(get_right_child(r)))



