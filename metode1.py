#program menggunakan cara kedua (dengan metode)

class Color():
	def __init__(self, r, g, b):
		self.r = r
		self.g = g
		self.b = b
	def value(self):
		return self.r, self.g, self.b

yellow = Color(255, 255, 0)
print(yellow.r)
print(yellow.value())