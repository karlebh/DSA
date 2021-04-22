class DiGraph:
	def __init__(self):
		self.graph = {}

	def addVertex(self, vertex):
		self.graph[vertex] = {}

	def addEdge(self, fromVertex, toVertex, weight):
		if weight == None:
			weight = 0

		self.graph[fromVertex][toVertex] = weight

	def removeEdge(self, fromVertex, toVertex):
		if self.graph[fromVertex] and self.graph[fromVertex][toVertex] != None:
			del self.graph[fromVertex][toVertex]

	def removeVertex(vertex):
		for adjVertex in self.graph[vertex]:
			self.removeEdge(adjVertex, vertex)
		del self.graph[vertex]

	def traverseBFS(self,vertex, fn):
		queue = []
		visited = {}

		queue.append(vertex)

		while len(queue):
			vertex = queue.pop(0)

			if not visited[vertex]:
				visited[vertex] = True
				fn(vertex)
