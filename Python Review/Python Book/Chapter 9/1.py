class Dog():
	def __init__(self, name, age):
		self.name = name
		self.age = age
		
	def sit(self):
		print(self.name + " is now sitting!")
		
		
sunny = Dog("Sunny", 4)
sunny.sit()
print(sunny.age)
