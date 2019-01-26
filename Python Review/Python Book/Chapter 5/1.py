cars = ["bmw", "audi", "mercedes"]

for each in cars:
	if each.upper() == "BMW" and each == "bmw":
		print("wow gangster")

if "mercedes" in cars:
	print("so rich")
	
if "prius" not in cars:
	print("you're the real mvp")

if "ferrari" in cars:
	print("best red car")
elif "lamborghini" in cars:
	print("best green car")
else:
	print("loser")

if cars: # true if items are in it
	print("list is not empty")
else:
	print("list is empty")
	
