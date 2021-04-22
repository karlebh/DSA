class Graph:
	def __init__(self, graphDictionary = None):
		if graphDictionary is None:
			graphDictionary = {}
		self.graphDictionary = graphDictionary

	def getVertices(self):
		return list(self.graphDictionary.keys())

	def edges(self):
		return self.findEdges()

	def findEdges(self):
		edgeName = []

		for vertex in self.graphDictionary:
			for nextVertex in self.graphDictionary[vertex]:
				if {nextVertex, vertex} not in edgeName:
					edgeName.append({vertex, nextVertex})
		return edgeName

	def addVertex(self, vertex):
		if vertex not in self.graphDictionary:
			self.graphDictionary[vertex] = {}

	def addEdge(self, edge):
		edge = set(edge)
		(vertex1, vertex2) = tuple(edge)
		if vertex1 in self.graphDictionary:	
			self.graphDictionary[vertex].append(vertex2)
		else:
			self.graphDictionary[vertex1] = [vertex2]

	def depthFirstSearch(self, start,visited = set()):
		
		if start not in visited:
			print(start)
			visited.add(start)
			for neighbour in self.graphDictionary[start]:
				self.depthFirstSearch(neighbour)

	def breadthFirstSearch(self, start):

		visited = set()
		queue = []
		visited.add(start)
		queue.append(start)

		while queue:
			firstQueueItem = queue.pop(0)
			print(firstQueueItem, end=' ')

			for neighbour in self.graphDictionary[firstQueueItem]:
				if neighbour not in  visited:
					visited.add(neighbour)
					queue.append(neighbour)

		





graphElements = {
	"a" : ["b", "c"],
	"b" : ["d", "e"],
	"c" : ["f"],
	"d" : [],
	"e" : ["f"],
	"f" : [],
}

graph = Graph(graphElements)
# print(graph.getVertices())
# print(graph.findEdges())
# print(graph.depthFirstSearch('a'))
print(graph.depthFirstSearch('a'))
print(graph.breadthFirstSearch('a'))