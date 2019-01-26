def formatYou(first, last):
	return (first + " " + last).title()
	
print(formatYou("marton", "zeisler"))

def squareList(list):
	del list[0]
	list = [each**2 for each in list]
	return list

myList = [1,2,3,4,5]
myList = squareList(myList[:]) # passing list by 
print(myList)
