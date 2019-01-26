# user input and while loop

age = int(input("Enter your name: "))
if age >= 18:
	print("You can drink")
else:
	print("You cannot drink")
	while True:
		age += 1
		print("You're " + str(age))
		if age < 18:
			print("You still can't drink buddy")
		else:
			print("yay go get drunk quick")
			break