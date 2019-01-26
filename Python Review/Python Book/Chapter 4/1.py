cities = ["budapest", "new york", "london", "paris"]

for each in cities:
	print(each, end=", ")
print("\n")

even = list(range(2,11, 2))

squares = [each**2 for each in range(1,11)]
print(squares)

#slicing a list
print(squares[::2])