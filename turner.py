class Config:

	def __init__(self, arr = [0, 1, 2, 3, 4, 5], path=''):
		self.array = arr
		self.path = path

	def __repr__(self):
		return f"""
| {self.array[0]} {self.array[1]} {self.array[2]} |
| {self.array[3]} {self.array[4]} {self.array[5]} |
"""

	def __eq__(self, other):
		for i in range(6):
			if self.array[i] != other.array[i]:
				return False
		return True

	def __ne__(self, other):
		return not self.__eq__(self, other)

	def r_turn(self):
		return Config([
			self.array[0], self.array[4], self.array[1],
			self.array[3], self.array[5], self.array[2]
		], self.path + 'R')
	
	def u_turn(self):
		return Config([
			self.array[3], self.array[0], self.array[2],
			self.array[4], self.array[1], self.array[5]
		], self.path + 'U')

class Tree:

	def __init__(self, seed):
		self.levels = [[seed]]

	def search(self, config):
		for level in self.levels:
			if config in level:
				return True
		else:
			return False

	def __iter__(self):
		return self

	def append_level(self, level):
		self.levels.append(level)

	def last_level(self):
		return self.levels[-1]

	def export(self):
		res = []
		for i in self.levels:
			res.extend(i)
		return res

	def pattern_match(self, str):
		arr = []
		for i in str:
			if i == '*':
				arr.append('*')
			else:
				arr.append(int(i))
		for config in self.export():
			works = True
			for t in range(6):
				if not (arr[t] == '*' or config.array[t] == arr[t]):
					works = False
			if works is True:
				return config
		return False

tr = Tree(Config())

while len(tr.last_level()) > 0:
	level = []
	for config in tr.last_level():
		if not (tr.search(config.r_turn()) or config.r_turn() in level):
			level.append(config.r_turn())
		if not (tr.search(config.u_turn()) or config.u_turn() in level):
			level.append(config.u_turn())
	tr.append_level(level)

if __name__ == '__main__':
	file = open('configs.txt', 'w')
	for config in tr.export():
		print(config)
		file.write(config.__repr__())
	file.close()