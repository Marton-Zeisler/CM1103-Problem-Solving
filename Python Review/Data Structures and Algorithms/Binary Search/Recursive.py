def binarySearch(myList, key, min, max):
	if min >= max:
		if myList[min] == key:
			return min
		else:
			return -1
	else:
		mid = (min + max) // 2
		if myList[mid] == key:
			return mid
		elif key < myList[mid]:
			return binarySearch(myList, key, min, mid-1)
		else:
			return binarySearch(myList, key, mid+1, max)


def startSearch(listData, item):
	return binarySearch(listData, item, 0, len(listData)-1)

print(startSearch([1,2,3,4,5,10,20,43,244], 43))


