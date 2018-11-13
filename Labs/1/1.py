import math
import statistics

# 6.
def timeFromSeconds(totalSec):
	seconds = totalSec % 60
	totalMinutes = totalSec // 60
	hours = totalMinutes // 60
	minutes = totalMinutes % 60
	print(str(hours) + ":" + str(minutes) + ":" + str(seconds))

#print(timeFromSeconds(6149))

# 7.
def totalSeconds(hours, minutes, seconds):
	return (hours * 60 * 60) + (minutes * 60) + seconds

#print(totalSeconds(2, 10, 2))

# 8.
def volumeSphere(radius):
	return (4/3) * math.pi * math.pow(radius,3)

print(volumeSphere(5))	

def bookCosts(copies):
	if copies <= 0:
		return
	
	return (24.95*0.4+3) + (24.95*0.4+0.75)*(copies-1)

#print(bookCosts(60))

# 9.
myList = list(range(10)) # [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
myList[1::2] = myList[::-2]
print(myList)

# 13
a = list(range(9, -1, -1))
print(len(a))
print(sum(a))
print(sum(a[:4]))
print(min(a))
print(max(a[::3]))
copyA = sorted(a)
print(copyA)

# 14
newList = [9, 3, 5, 4, 10, 4, 3, 2, 4]
print(statistics.mean(newList))
print(statistics.median(newList))
print(statistics.mode(newList))

# 15
for char in "1bc4":
	if not char.isalpha():
		print("not a letter")
	else:
		print(char.upper())
	
	
	
	
	
	
	
	
	
	
	
	
	
	