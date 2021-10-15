#program menggunakan cara ketiga (dengan atribut/variabel dan metode)

class Color():
	def __init__(self, r, g, b):
		self.r = r
		self.g = g
		self.b = b
		self.get_value()
	def get_value(self):
		self.value = self.r, self.g, self.b
	def ubah_r(self, warna):
		self.r = warna
		self.get_value()
	def ubah_g(self, warna):
		self.g = warna
		self.get_value()
	def ubah_b(self, warna):
		self.b = warna
		self.get_value()


yellow = Color(255, 255, 0)
print(yellow.r)
print(yellow.g)
print(yellow.b)
print(yellow.value)
