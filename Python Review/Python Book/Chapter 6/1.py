# dictionaries

people = {"marci": 20, "balint": 16}
people["vicky"] = "designer"
print(people["vicky"])
del people["vicky"]
print(people)

for key in people: #looping through the keuys
	print(key)

print(list(people.keys()))

for key, value in people.items():
	print(key + " - " + str(value), end=", ")
print()


