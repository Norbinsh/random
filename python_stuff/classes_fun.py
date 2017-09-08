"""
Everything's an object! i.e has methods and values.
Everything is based on a class, i.e the blue print of an object. 
"""

x = "Shay"
print(dir(x))

class Vehicle:
	"""docstring here"""

	def __init__(self, color, doors, tires, vtype):
		"""Constructor"""
		self.color = color
		self.doors = doors
		self.tires = tires
		self.vtype = vtype

	def brake(self):
		"""Stop the car"""
		return "{} breaking".format(self.vtype)

	def drive(self):
		"""Drive the car"""
		return "I am driving {} {}".format(self.color, self.vtype)

if __name__ == '__main__':
	car = Vehicle("Blue", 5, 4, "car")
	print(car.brake())
	print(car.drive())

	truck = Vehicle("Red", 3, 6, "truck")
	print(truck.brake())
	print(truck.drive())


class Car(Vehicle):
	"""The Car class"""

	def brake(self):
		return "The car class is breaking"

	# def drive(self):
	# 	return "I am driving {} {} with {} doors and {} tires".format(
	# 		self.color, self.vtype, self.doors, self.tires)

if __name__ == '__main__':
	car = Car("Yellow", 2, 4, "car")
	print(car.brake())
	print(car.drive())

""" Notice the inheritance used, the way I overided the brake method, etc """