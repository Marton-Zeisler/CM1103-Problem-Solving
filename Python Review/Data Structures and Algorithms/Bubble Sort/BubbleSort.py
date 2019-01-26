def sort(listData):
	length = len(listData)
	for i in range(length):
		for j in range(0, length-i-1):
			if listData[j] > listData[j+1]:
				listData[j], listData[j+1] = listData[j+1], listData[j]
				

myList = [2,1,44,2,144,43,12,122]

sort(myList)

print(myList)