



class Rectangle():
	def __init__(self, length, width, height):
		self.length = length
		self.height = height
		self.width = width
	def __str__(self):
		return f'Length is {self.length}, width is {self.width} and height is {self.height}.'
	    # nel cor piu non mi sento
	def __add__(self, other):
		return self.length * self.width * self.height + other.length * other.height * other.width
a = Rectangle(15, 10, 5)	
print(a)
b  = Rectangle(5, 10, 15)
print(a.__add__(b))