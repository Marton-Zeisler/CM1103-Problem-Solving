class Car():
	def __init__(self, make, model, year):
		self.make = make
		self.model = model
		self.year = year
		self.miles = 0
	
	def get_descriptive_name(self):
		long_name = str(self.year) + " " + self.make + " " + self.model
		return long_name.title()
		
	def read_odemeter(self):
		print("This car has " + str(self.miles) + " miles on it.")
		
	def add_miles(self, miles):
		self.miles += miles
		

class ElectricCar(Car):
	def __init__(self, make, model, year):
		super().__init__(make, model, year)
		
	
	
myTesla = ElectricCar("tesla", "model s", 2018)
print(myTesla.get_descriptive_name())