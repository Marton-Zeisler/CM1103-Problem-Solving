def recPower(a,n):
	if n == 0:
		return 1
		
	if n == 1:
		return a
	
	if n % 2 == 0:
		return recPower(a, n / 2) * recPower(a, n / 2)
	else:
		return a * recPower(a, n-1)
	
	
	
print(recPower(2, 0))