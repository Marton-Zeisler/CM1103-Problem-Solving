# 1
def Q1():
	sports = ["football", "rugby", "hockey", "tennis"]
	print(sports[0])
	print(sports[-1])
	sports.append("cycling")
	print(len(sports))

	for each in sports:
		print(each[0], end=" ")
		
	sports.remove("football")
	print(sports)
	newList = sports[len(sports)//2-1:len(sports)//2-1+2]
	print(newList)
	
# Q1()

def Q2():
	myList = ["a", "b", "c", "d", "e"]
	del myList[3]
	del myList[0]
	print(myList)
	
# Q2()

# 3
def Q3():
	square = lambda n : n * n
	print(square(2))

# Q3()

# 4
def Q4():
	a = [2, -6, -5, 3, 9]
	a = sorted(a)
	a = sorted(a, key=lambda x : -x)
	a = sorted(a, key=lambda x : abs(x))
	a = sorted(a, key=lambda x : x % 2)
	print(a)
	a = sorted(a, key=lambda x : (x % 2, x)) # sorts by remainder of 2 and then by x
	print(a)
	
#Q4()

# 5
def Q5():
	a = ["tim", "bob", "trevir", "susan","anna"]
	a = sorted(a, key=lambda a : a[0])
	a = sorted(a, key=lambda a : a[1])
	a = sorted(a, key=lambda a : a[-1])
	a = sorted(a, key=lambda a : len(a))
	a = sorted(a, key=lambda a : (len(a), a[0])) #sorted by length of each name, ties decided by alpabetcal order
	a = sorted(a, key=lambda a: (a[0]!="a", a[0]!="e", a[0]!="u", a[0]!="i", a[0]!="o"), reverse=True)
	print(a)
	
# Q5()

# 6
def Q6(rows,columns):
	for each in range(0, rows):
		for each in range(0,columns):
			print("*", end=" ")
		print()
		
# Q6(2, 4)

# 7
def Q7():
	weights = [750, 387, 291, 712, 100, 622, 109, 750, 282]
	total = 0
	counter = 0
	while (total+weights[counter]) < 3000 and counter < len(weights):
		total += weights[counter]
		print(str(weights[counter]) + "kg was added.")
		counter += 1

	print("Capacity reached. Total weight is " + str(total) + "kg.")

# Q7()

# 8
def Q8():
	width = int(input("Enter width: "))
	height = int(input("Enter height: "))
	Q6(height, width)
	
#Q8()

# 9
def Q9():
	a = [1,2,3,4]
	b = [3,4,5,6]
	unionOfSet = set(a+b)
	print(unionOfSet)
	
	intersectionOfSet = []
	for each in a:
		if each in b:
			intersectionOfSet.append(each)
	print(intersectionOfSet)
	
	subtractA_B = []
	for each in a:
		if each not in b:
			subtractA_B.append(each)
	print(subtractA_B)
	
	subtractB_A = []
	for each in b:
		if each not in a:
			subtractB_A.append(each)
	subtractA_B_Add_subtractB_A = subtractA_B + subtractB_A
	print(subtractA_B_Add_subtractB_A)
	
	print(a)
	
	
#Q9()

