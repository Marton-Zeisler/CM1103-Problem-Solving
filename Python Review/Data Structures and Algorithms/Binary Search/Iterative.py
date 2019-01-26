def binarySearch(listData, value):
	low = 0
	high = len(listData)-1
	while low <= high:
		mid = (low + high) // 2
		if listData[mid] == value:
			return mid
		elif listData[mid] < value:
			low = mid + 1
		else:
			high = mid - 1
			
	return -1
	


print(binarySearch([1,3,9,11,15,19,29], 22))