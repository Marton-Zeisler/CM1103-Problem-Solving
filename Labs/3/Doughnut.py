def badGuestNumbers():
	numbers = []
	
	for each in range(1,101):
		if each % 3 == 0 or each % 20 == 0:
			continue
		
		counter = each
		while counter >= 0:
			counter -= 20
			if counter % 3 == 0:
				break
			else:
				numbers.append(each)
				
	
	return numbers
	
print(badGuestNumbers())
