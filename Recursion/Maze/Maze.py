class Maze:
	def __init__(self, file_name):
		rows = 0
		columns = 0
		self.maze_list = []
		file = open(file_name, "r")

		for line in file:
			row_list = []
			column = 0 #it is different from column with an "s" above
			for character in line[:-1]:
				row_list.append(character)
				if character == "S":
					self.start_row = rows
					self.start_column = column
				column = column + 1
			rows = rows + 1
			self.maze_list.append(row_list)
			columns = len(row_list)

