class Account():
	def __init__(self, cardNumber, balance):
		self.cardNumber = cardNumber
		self.balance = balance
	
	def addBalance(self, amount):
		self.balance += amount
	
	def subtractBalance(self, amount):
		self.balance -= amount
	