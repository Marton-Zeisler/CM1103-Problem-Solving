import csv
import re

# 1
def Q1():
	d = 50506.2124524342352525242
	print("The value of d is {0:10.2f}".format(d))
	print("%.2f" % d)
	integer1 = int(input("Enter an integer: "))
	print("{0:x}".format(integer1))
	integer2 = int(input("Enter an integer: "))
	print("{0:b}".format(integer2))

# Q1()

# 2
def Q2():
	a = "animal"
	b = "horse"
	print("My faovourite {} is {}".format(a,b))

# Q2()

# 3
def Q3_writeCurrency(currency, amount):
	return currency + "{0:.2f}".format(amount)
	
	
#print(Q3_writeCurrency("$", 50.2597))

# 4
def Q4():
	d = {"Tom" : 500, "Stuart" : 1000, "Bob" : 55, "Dave" : 21274}
	del d["Bob"]
	d["Phil"] = 24
	print("Number of items: " + str(len(d)))
	print("List of keys: " + str(list(d.keys())))
	print("List of values: " + str(list(d.values())))
	print("Dave" in d)
	print("Peter" in d)
	print(500 in d)
	
	for each in d:
		print(each, end=" ") # prints the keys only
	
	print()
	
	for key,value in d.items():
		print(key, value, end=" ")

# Q4()

# 5
def Q5():
	cities = {}
	with open("towns.csv") as csvfile:
		reader = csv.reader(csvfile)
		for each in reader:
			cities[each[0]] = int(each[1])
			if int(each[1]) >= 500000 and int(each[1]) <= 1000000:
				print("{} : {}".format(each[0], each[1]))
		
		print()
		print()
		print()
		city_Tuples = []
		for city, population in cities.items():
			city_Tuples.append((city, population))
		city_Tuples = sorted(city_Tuples, key=lambda x: -x[1])
		
		for city, population in city_Tuples:
			print("{} : {}".format(city, population))
			
# Q5()

# 6
def Q6(text):
	letterList = {}
	for each in text:
		if each in letterList:
			letterList[each] += 1
		else:
			letterList[each] = 1
	
	return letterList

#print(Q6("I am not sure what I am doing"))


# 7
def Q7(text):
	result = re.match("[a-z]+", text)
	if result != None:
		print("Matched!")
	else:
		print("Not Matched!")
		

# Q7("i am very happy")

# 8
def Q8(text):
	result = re.match("[a-z]+@[a-z]+.[a-z]{3}", text)
	if result != None:
		print("Matched!")
	else:
		print("Not Matched!")
	
Q8("mar@gmail.com")
