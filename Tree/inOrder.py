def inOrder(tree):
	if tree != None:
		inOrder(tree.getLeftChild())
		print(tree.getRoootValue())
		inOrder(tree.getRightChild())
