def printLightStates(lights):
	for index, value in enumerate(lights):
		print("Light #" + str(index+1) + ": " + str(value))
		

lights = [False]*50

for each in range(0, len(lights)):
	for each2 in range(each, len(lights), each+1):		
		lights[each2] = not lights[each2]

printLightStates(lights)
