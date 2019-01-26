import hello
from hello import greet as gr

def addNumbers(*numbers):
	total = 0
	for each in numbers:
		total += each
	
	return total	
	
	
print(addNumbers(1,2,3,4,5))
hello.greet()
gr()