class BinaryHeap:
	def __init__(self):
		self.heapList = [0]
		self.currentSize = 0

	def percolateUp(self, i):
		while i // 2 > 0:
			if self.heapList[i] < self.heapList[i // 2]:
				# temp = self.heapList[i // 2]
				# self.heapList[i // 2] = self.heapList[i]
				# self.heapList[i] = temp
				self.heapList[i // 2], self.heapList[i] = self.heapList[i], self.heapList[i // 2]

			i //= 2

	def insert(self, node):
		self.heapList.append(node)
		self.currentSize += 1
		self.percolateUp(self.currentSize)

	def percolateDown(self, i):
		while (i * 2) <= self.currentSize:
			minChild = self.minChild(i)
			if self.heapList[i] > self.heapList[minChild]:
				# temp = self.heapList[i]
				# self.heapList[minChild] = self.heapList[i]
				# self.heapList[i] = temp
				self.heapList[i], self.heapList[minChild] = self.heapList[minChild], self.heapList[i]
			i = minChild

	def minChild(self, i):
		if i * 2 + 1 > self.currentSize:
			return i * 2
		else:
			if self.heapList[i * 2] < self.heapList[i * 2 + 1]:
				return i * 2
			else:
				return i * 2 + 1

	def deleteMin(self):
		min = self.heapList[1]
		self.heapList[1] = self.heapList[self.currentSize]
		self.currentSize = self.currentSize - 1
		self.heapList.pop()
		self.percolateDown(1)
		return min

	def buildHeap(self, list):
		i = len(list) // 2
		self.currentSize = len(list)
		self.heapList = [0] + list[:]
		while i > 0:
			self.percolateDown(i)
			i = i - 1