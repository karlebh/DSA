class UndiGraph:
	def __init__(self):
		self.edges = {}

	def addVertice(self, vertex):
		self.edges[vertex] = {}

	def addEdge(self, vertex1, vertex2, weight):
		if weight == None:
			weight = 0

		self.edges[vertex1][vertex2] = weight
		self.edges[vertex2][vertex1] = weight

	def removeEdge(self, vertex1, vertex2):
		if self.edges[vertex1] and self.edges[vertex1][vertex2] != None:
			del self.edges[vertex1][vertex2]

		if self.edges[vertex2] and self.edges[vertex2][vertex1] != None:
			del self.edges[vertex2][vertex1]

	def removeVertex(self, vertex):
		for adjVertex in self.edges[vertex]:
			self.removeEdge(adjVertex, vertex)
		del self.edges[vertex]


	def echo(self):
		print(self.edges)

ug = UndiGraph()
ug.addVertice(1)
ug.addVertice(2)
ug.removeVertex(1)
ug.addVertice(3)
ug.addVertice(4)
ug.echo()

ug.addEdge(2, 3, 2)
ug.addEdge(3, 4, 10)
ug.echo()
