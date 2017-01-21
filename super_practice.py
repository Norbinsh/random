"""
MRO, Method resolution order shows an ordered list of types that our class 
is derived from. starting from 'object' base class.class_var

super allows us to access inherited methods that was overriden in a class,
we can refer to the parent class/classes without actually naming them, 
so in case and you edit your code in the future and you rename the classes, 
you won't need to actually edit the class names in the code itself. 

additional use case may be an hybrid inheritance from several classes. 
"""

class Base:
	class_var = "my Base class var"
	var = 5

	def __init__(self):
		print("I AM BASE")


class X(Base):
	class_var = 'my X class var'
	def __init__(self):
		print('X')
		super().__init__()


class Y(Base):
	var = 10
	class_var = 'my Y class var'
	def __init__(self):
		print('Y')
		super().__init__()


class Z(X, Y):
	pass

# print(Base.__mro__)
# print(Z.__mro__)
# print(X.__mro__)
print(X())

# print(super(X, X).var)
# print(super(Z, Z).var)
# print(super(Z, Z).class_var)
# print(Z.var)

class Base():
	def __init__(self):
		s = super()
		print(s.__thisclass__)
		print(s.__self_class__)
		s.__init__()

class SubClass(Base):
	pass

sub = SubClass()