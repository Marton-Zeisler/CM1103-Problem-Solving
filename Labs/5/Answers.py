import matplotlib.pyplot as plt
import MyRandom
import re
	
# Q1
def Q1():
	examMarks = [25,72,83,91,61]
	plt.plot(list(range(1, len(examMarks)+1)), examMarks, "ro") # plotting arg1 on x-axis and arg2 on y-axis and arg3 adding style
	plt.axis([0, len(examMarks)+5,0,100]) # [xmin, xmax, ymin, ymax]
	plt.xticks(list(range(len(examMarks)+6)))
	plt.xlabel("Student ID")
	plt.ylabel("Score")
	plt.show()
	
#Q1()

# Q2
def Q2():
	examMarks = [25,72,83,91,61]
	cwkMarks = [56, 90, 45, 62, 60]
	plt.plot(examMarks, cwkMarks, "bo")
	plt.axis([0,100,0,100])
	plt.xlabel("Exam Marks")
	plt.ylabel("Coursework Marks")
	plt.show()
	
#Q2()

# Q3
def Q3():
	examMarks = [25,72,83,91,61]
	cwkMarks = [56, 90, 45, 62, 60]
	plt.plot(examMarks, cwkMarks, "bo")
	plt.axis([0,100,0,100])
	plt.xlabel("Exam Marks")
	plt.ylabel("Coursework Marks")
	#fig = plt.figure()
	#ax = fig.add_subplot(111)
	plt.show()

#Q3()

# Q4
def Q4(n):
	randNumbers = []
	for each in range(n):
		currentNumber = MyRandom.random()
		randNumbers.append(currentNumber)
	
	return randNumbers
		
#print(Q4(50))

# Q6
def Q6(numbers):
	period = 0
	for each in range(1,len(numbers)):
		if numbers[each] == numbers[0]:
			period = each
			break
	return period
	

#print(Q6(Q4(100)))

# 9

class MyName:
	def __init__(self):
		print("init")
		self.age = 12
		
	def __repr__(self):
		print(self.age)
		return "{:s} {:s} {:s}".format(self.firstname, self.middlename, self.surname) 
		
	def printMe(self):
		print("{:s} {:s}".format(self.firstname, self.surname))

me = MyName()
me.firstname = "Marton"
me.surname = "Zeisler"
me.middlename = "Josh"
#print(hasattr(me, "middslename")) # checks if the object has a property
#print(me)


# 11
def myReverse(data):
	for index in range(len(data)-1,-1,-1):
		yield data[index]

myList = [1,2,4,8,16,32,64,128,256,512,1024]

def Q11(data):
	for i in myReverse(data):
		print(i)
		
#Q11(myList)

def myNth(data, n):
	for index in range(0, len(data), n):
		yield data[index]
	
def Q11_a(data, n):
	for i in myNth(data, n):
		print(i)
		
#Q11_a(myList, 2)

# Q13
def Q13():
	# a
	a = "c1841485"
	if re.match("^c[0-9]{7}$", a):
		print("Username valid")
	else:
		print("Username invalid")
	
	# b
	b = "scm7uii"
	if re.match("^scm[0-9]{1}[a-z]{2,3}$", b):
		print("Old Username valid")
	else:
		print("Old Username invalid")
		
	# c
	c = "09-97-62"
	if re.match("^[0-9]{0,2}-+[0-9]{0,2}-[0-9]{0,2}$", c):
		print("Bank sort code valid")
	else:
		print("Bank sort code invalid")
		
	# d
	d = "BD51SMR"
	if re.match("^[A-Z]{2}[0-9]{2}[A-Z]{3}$", d):
		print("Car number valid")
	else:
		print("Car number invalid")
	
Q13()

if re.match("^[a-z]{2}$", "aaa"):
	print("valid")
else:
	print("invalid")


