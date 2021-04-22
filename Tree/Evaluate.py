import operator

def Evaluate(parseTree):
	opers = {'+' : operator.add, '-' : operator.sub, '*' : operator.mul, '/' : operator.truediv }

	left = parseTree.getLeftChild()
	right = parseTree.getRightChild()

	if left and right:
		fn = opers[parseTree.getRoootValue()]
		return fn(Evaluate(left), Evaluate(right))
	else:
		return parseTree.getRoootValue()
