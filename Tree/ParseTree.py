from BinaryTree import BinaryTree

def ParseTree(expression):
	expressionList = expression.split()
	stack = Stack() #Stack needs to be imported
	expressionTree = BinaryTree('') #BinaryTree needs to be imported
	stack.push(expressionTree)
	currentTree = expressionTree

	for i in expressionList:
		if i == "(":
			expressionTree.insertLeft('')
			stack.push(currentTree)
			currentTree = currentTree.getLeftChild()
		elif i not in ['*', '+', '-', '/', ')']:
			currentTree.setRootValue(int(i))
			parent = stack.pop()
			currentTree = parent
		elif i in ['*', '+', '-', '/']:
			currentTree.setRootValue(i)
			currentTree.insertRight('')
			stack.push(currentTree)
			currentTree = currentTree.getRightChild()
		elif i == ')':
			currentTree = stack.pop()
		else:
			raise ValueError
	return expressionTree

	pt = ParseTree("( ( 2 * 2 ) + 1 ) ")
	pt.postOrder()

