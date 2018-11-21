import csv

# Q1
def counting(i):
	print(i)
	i += 2
	print(i)
	i += 2
	print(i)
	if i == 1022:
		print(i+2)
		return
	counting(i)
	
#counting(2)

# Q2
def fib(n):
	if n == 0:
		return 0
	if n == 1:
		return 1
	return fib(n-1) + fib(n-2)
	
#print(fib(6))

# Q3
def printList(a):
	while len(a) > 0:
		print(a.pop(0))

list = [1,2,3]
#printList(list[:])
#printList(list[:])
#print("Length of origincal list is: " + str(len(list)))

# Q4
def Q4():
	with open("facup.csv") as csvfile:
		rdr = csv.reader(csvfile)
		for row in rdr:
			print(row[0] + " last won in " + row[1])
			print(type(row[1]))
			year = int(row[1])
			print(year % 2 == 0)


#Q4()

# Q5
def Q5():
	with open("MultipleTourWinners.csv") as csvfile:
		reader = csv.reader(csvfile)
		for row in reader:
			print(row[0] + ", " + row[2])
	
#Q5()

# Q6
def Q6():
	for n in range(0,101, 2):
		print(n)

def Q6_2():
	allSeasons = ["Spring", "Summer", "Autumn", "Winter"]
	for (i, season) in enumerate(allSeasons):
		print(i, season)

#Q6()
# Q6_2()

# Q7
def Q7():
	with open("MultipleTourWinners.csv") as csvfile:
		reader = csv.reader(csvfile)
		for (index, row) in enumerate(reader):
			wins = int(row[2])
			if wins >= 3:
				print(index, row[0],row[1], row[2])
				
# Q7()

# Q8
def Q8():
	mark = int(input("Enter mark: "))
	if mark >= 50 and mark < 60:
		print("Result is 2:2")
	
	for n in range(1, 11):
		print(n**2)
	
#Q8()

	
