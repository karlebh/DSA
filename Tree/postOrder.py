def postOrder(tree):
	if tree != None:
		postOrder(tree.getLeftChild())
		postOrder(tree.getRightChild())
		print(tree.getRoootValue())