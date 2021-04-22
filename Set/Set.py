class Set:
	def __init__(self):
		self.store = {}

	def add(self, data):
		if data not in self.store :
			self.store.append(data)
		else:
			return "Duplicate not allowed"

	def has(self, data):
		if data in self.store:
			return True
		else:
			return False

	def remove(self, data):
		if data in self.store:
			self.store.remove(data)
		else:
			return "Data not in Set"

	def union(self, otherSet):

		for item in self.store:
			if item not in otherSet:
				otherSet.append(item)
		return otherSet

	def difference(self, otherSet):
		
		for item in self.store:
			if item in otherSet:
				otherSet.remove(item)
		return otherSet

	def interset(self, otherSet):
		interset = []

		for item in self.store:
			if item in otherSet:
				interset.append(item)
		return interset

	def SuperSet(self, otherSet):

		isSuperSet = False
		for item in otherSet:
			if item in self.store:
				isSuperSet = True

		return isSuperSet

	def SubSet(self, otherSet):

		isSubSet = False
		for item in self.store:
			if item in otherSet:
				isSubSet = True
				
		return isSubSet



a = Set()
b = Set()
print(a)

a.SubSet(b)
# a.SuperSet(b)
				



			

