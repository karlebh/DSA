class Node:
	def __init__(self, root):
		self.root = root
		self.leftChild = None
		self.rightChild = None

	def insertLeft(self, Node):
		if self.leftChild == None:
			self.leftChild = Node(Node)
		else:
			node = Node(Node)
			node.leftChild = self.leftChild
			self.leftChild = node

	def insertRight(self, Node):
		if self.rightChild == None:
			self.rightChild = Node(Node)
		else:
			node = Node(Node)
			node.rightChild = self.rightChild
			self.rightChild = node

	def getRightChild(self):
		return self.rightChild

	def getLeftChild(self):
		return self.leftChild

	def setRootValue(self, value):
		self.root = value

	def getRoootValue(self):
		return self.root

	def preOrder(self):
		print(self.root)
		if self.leftChild:
			self.leftChild.preOrder()
		if self.rightChild:
			self.rightChild.preOrder()
	


