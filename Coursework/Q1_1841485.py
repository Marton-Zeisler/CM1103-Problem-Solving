import csv
import random

# a
def series_score(results, discards=1):
	# results is a tuple of a string and a list of integers
	positions = sorted(results[1])
	
	# deleting as many highest scores as given discards
	for each in range(0, discards):
		del positions[-1]

	return sum(positions)
	
#print(series_score(("Bob", [2,4,1,1,2,5]), 2))


# b
def sort_series(sailorsResults):
	# sorting the list using series_score() and breaking ties by comparing first race result
	sailorsResults.sort(key=lambda x: (series_score(x), x[1][0]) )
	
	return sailorsResults

#print(sort_series( [("Alice", [1, 2, 1, 1, 1, 1]), ("Bob",   [3, 1, 5, 3, 2, 5]), ("Clare", [2, 3, 3, 2, 4, 2]), ("Dennis", [5, 4, 4, 4, 3, 4]), ("Eva", [4, 5, 3, 5, 5, 3])]))


# c
def read_sailor(csvFileName):
	# creating an empty dictionary
	sailors = {} 
	
	# reading the csv file
	with open(csvFileName) as csvfile:
		reader = csv.reader(csvfile)
		next(reader, None) # skipping the headers
		for each in reader:
			# [name, performance score, standard deviation
			# populating our dictionary with the values
			sailors[each[0]] = (float(each[1]), float(each[2]))
	
	return sailors
			
#print(read_sailor("sailors.csv"))


# d
def generate_performance(sailorsSpecs):
	# creating an empty dictionary
	sailors = {}

	for key, value in sailorsSpecs.items():
		# calculating the random performace score based on the tuple's mean and std deviation
		sailors[key] = random.normalvariate(value[0], value[1])
		
	print(sailors)
	return sailors

print(generate_performance(read_sailor("sailors.csv")))
	
# e
def calculate_finishing_order(sailorsPerfs):
	# Creating a list of tuples of sailor name and performance score
	sailors = list(sailorsPerfs.items())
	# sorting the tuples by their performance score
	sailors.sort(key=lambda x: x[1], reverse=True)
	# getting the first element(sailor name) of each tuple
	names = [each[0] for each in sailors]
	
	#print(sailors)
	return names
	
		
#print(calculate_finishing_order(generate_performance(read_sailor("sailors.csv"))))


# f
def runRound(sailors):
	# calculating a new random performance score for each race
	performances = generate_performance(read_sailor("sailors.csv"))
	# getting an ordered list of the sailors after generating their performance scores
	finishedRound = calculate_finishing_order(performances)

	# at the beginning sailors will be a dictionary with sailor names as keys and empty lists as values
	# we append the finished position for each sailor after the race is now complete
	# calculate_finishing_order function returns a list of sailor names in order and I use the indices of that list to determine the finishing position for each sailor
	for index, value in enumerate(finishedRound):
		sailors[value].append(index+1)
	
	
def startRace(sailors, rounds):
	# runninng the race rounds times
	for each in range(0, rounds):
		runRound(sailors)
		#print("Round #" + str(each+1) + ": " + str(sailors))
	
	# At this point, we ran rounds amount of races and appended the race result position for each sailor's array in the sailors dictionary
	print(sailors)
	
	# converting the dictionary into a list of tuples of sailor name and list of positions
	sailorTuples = []
	for key, value in sailors.items():
		sailorTuples.append((key,value))
	
	# sorting the tuple list
	sort_series(sailorTuples)	
	#print(sailorTuples)
	
	# Getting the sailor names from the tuples and putting it in a list
	namesInOrder = [each[0] for each in sailorTuples]
	return namesInOrder

results = {"Alice": [], "Bob": [], "Clare": [], "Dennis": [], "Eva": []}

#print("\n\nFinal Result: " + str(startRace(results , 6)))
