import TreeNode

class BST:

	def __init__(self):
		self.root = None
		self.size = 0

	def length(self):
		return self.size

	def __len__(self):
		return self.size

	def __iter__(self):
		return self.root.__iter__()

	def put(self, key, value):
		if self.root:
			self._put(key, value, self.root)
		else:
			self.root = TreeNode(key, value)
		self.size = self.size + 1

	def _put(self, key, value, currentNode):
		if key < currentNode.key:
			if currentNode.hasLeftChild():
				self._put(key, value, currentNode.leftChild)
			else:
				currentNode.leftChild = TreeNode(key, value, parent = currentNode)
		else:
			if currentNode.hasRightChild():
				self._put(key, value, currentNode.rightChild)
			else:
				currentNode.rightChild = TreeNode(key, value, parent = currentNode)

	def __setitem__(self, key, value):
		self.put(key, value)

	def get(self, key):
		if self.root:
			result = self._get(key, self.root)
			if result:
				return result.value
			else:
				return None
		else:
			return None

	def _get(self, key, currentNode):
		if not currentNode:
			return None
		elif currentNode.key == key:
			return currentNode
		elif key < currentNode:
			return self._get(key, currentNode.leftChild)
		else:
			return self._get(key, currentNode.rightChild)

	def __getitem__(self, key):
		return self.get(key)

	def __contains__(self, key):
		if self._get(key, self.root):
			return True
		else:
			return False

	def delete(self, key):
		if self.size > 1:
			nodeToRemove = self._get(key, self.root)
			if nodeToRemove:
				self.remove(nodeToRemove)
				self.size = self.size - 1
			else:
				raise KeyError('Node\'s key found in tree')
		elif self.size == 1 and self.root.key == key:
			self.root = None
			self.size = self.size - 1
		else:
			raise KeyError('Node\'s key found in tree')

	def __delitem__(self, key):
		self.delete(key)

	def spliceOut(self):
		if self.isLeaf():
			if self.isLeftChild():
				self.parent.leftChild = None
			else:
				self.parent.rightChild = None
		elif self.hasAnyChild():
			if self.hasLeftChild():
				if self.isLeftChild():
					self.parent.leftChild = self.leftChild
				else:
					self.parent.rightChild = self.leftChild
				self.leftChild.parent = self.parent
			else:
				if self.isLeftChild():
					self.parent.leftChild = self.rightChild
				else:
					self.parent.rightChild = self.rightChild
				self.rightChild.parent = self.parent

	def findSuccessor(self):
		successor = None
		if self.hasRightChild():
			successor = self.parent
		else:
			self.parent.rightChild = None
			successor = self.parent.findSuccessor()
			self.parent.rightChild = self
		return successor

	def findMin(self):
		current = self
		while current.hasLeftChild():
			current = current.left
		return current

	def findMax(self):
		current = self
		while current.hasRightChild():
			current = current.right
		return current

	def remove(self, Node):
		pass

