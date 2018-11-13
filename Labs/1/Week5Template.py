import doctest

# *** DO NOT CHANGE CODE ABOVE THIS LINE ***

def doomsday(y):
	"""
	>>> doomsday(2012)
	3
	>>> doomsday(1899)
	2
	>>> doomsday(1923)
	3
	>>> doomsday(10000)
	-1
	>>> doomsday(1756)
	-1
	>>> type(doomsday(2010))
	<class 'int'>
	"""
	
	x = 0
	if y >= 1800 and y <= 1899:
		x = 5
	elif y >= 1900 and y<= 1999:
		x = 3
	elif y >= 2000 and y <= 2099:
		x = 2
	elif y >= 2100 and y <= 2199:
		x = 0
	else:
		return -1
		
	w  = int(str(y)[-2:])
	
	b = w % 12
	a = w // 12
	c = b // 4
	sumABC = a + b + c
	d = sumABC % 7
	x = (x + d) % 7
	return x
		
