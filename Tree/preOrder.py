def preOrder(tree):
	if tree:
		print(tree.getRoootValue())
		preOrder(getLeftChild())
		preOrder(getRightChild())

