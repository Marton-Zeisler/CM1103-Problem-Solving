#Define the empty class PhoneBookEntry here

class PhoneBook:
	def __init__(self):
		self.data=dict()	
	
	def addEntry(self,name,number,email):
		self.data[name]=PhoneBookEntry()
		self.data[name].number= number
		self.data[name].email= email

	def delEntry(self,name):
		self.data.pop(name, None)
	
	def exist(self, name):
		return name in self.data

	def printBook(self):
		for key, value in self.data.items():
			print("Name: " + key + ", Number: " + value.number + ", Email: " + value.email)
	

class PhoneBookEntry: pass

myPhoneBook = PhoneBook()
myPhoneBook.addEntry("Marton Zeisler", "92923929", "mar@zeis.com")
myPhoneBook.addEntry("Vicky Vo", "78473y73", "vicky@vo.com")
print(myPhoneBook.exist("Vicky Vo"))
myPhoneBook.delEntry("Marton Zeisler")
print(myPhoneBook.exist("Marton Zeisler"))
myPhoneBook.printBook()
	