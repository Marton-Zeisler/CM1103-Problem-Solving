import matplotlib.pyplot as plt
from Q1_1841485 import *
import numpy as np

def calculateAverageScores(raceNumbers, discardComparison=False):
	# this function will calculate the average performance score for each sailor for each sets of races
	# raceNumbers parameter is a list of race numbers
	# the second parameter is an optinoal boolean, indicating whether we want to analyse how changing the number of discarded worst scores impact our results
	
	# to make sure we keep the performance scores in the same order as the names of sailors, we need to save their order by keeping track which index they are at
	nameIndexes = {"Alice": 0, "Bob": 1, "Clare": 2, "Dennis": 3, "Eva": 4}
	
	# the following lists will contain our results that we will return
	sailorsAverageScores = []
	sailorsAverageScores_Discard0 = []
	sailorsAverageScores_Discard2 = []
	
	# going through each set of races
	for raceNumber in raceNumbers:
		# the dictionary below will hold each sailor's score in the current simulation
		roundScores = {"Alice": [], "Bob": [], "Clare": [], "Dennis": [], "Eva": []}
		
		# going through as many rounds as specified in each simulation
		for round in range(0, raceNumber):
			roundScore = generate_performance(read_sailor("sailors.csv")) # generating the random score for each sailor for each race
			for sailorName, score in roundScore.items():
				roundScores[sailorName] += [score] # appending the score for each sailor

		# Calculating average performance score after the rounds are finished
		roundAverages = [0] * 5
		if discardComparison:
			roundAverages_Discard0 = [0] * 5
			roundAverages_Discard2 = [0] * 5
		
		# the following loop goes through each sailor's list of scores for the given set of races and calculate the average
		for sailorName, score in roundScores.items():
			if discardComparison:
				# calculating the average without removing any worst scores for the 2nd graph
				average_D0 = int(sum(score) / float(len(score)))
				roundAverages_Discard0[nameIndexes[sailorName]] = average_D0
				
				# removing the worst 2 race results for the 3rd graph
				score_D2 = sorted(score, reverse=True)
				del score_D2[-2:]
				average_D2 = int(sum(score_D2) / float(len(score_D2)))
				roundAverages_Discard2[nameIndexes[sailorName]] = average_D2
								
			# Removing the worst race result and calculaating the average for the 1st graph
			score = sorted(score, reverse=True)
			del score[-1]
			average = int(sum(score) / float(len(score)))
			roundAverages[nameIndexes[sailorName]] = average
		
		sailorsAverageScores += [roundAverages] # roundAverages holds a list of each sailors' average performance score for the current simulation
				
		if discardComparison:			
			sailorsAverageScores_Discard0 += [roundAverages_Discard0]
			sailorsAverageScores_Discard2 += [roundAverages_Discard2]
			
		
	
	if discardComparison:
		return [sailorsAverageScores, sailorsAverageScores_Discard0, sailorsAverageScores_Discard2]
	else:
		return [sailorsAverageScores]
		
	#return scores
	#[[100,80,70,60,40], [...], [...] ]
	#[ [Alice-race6-average, Bob-race6-average], [Alice-race36-average, Bob-race36-average...] ...  ]
	

def drawGraph(scores, title):
	# Configuring the graph
	n_groups = 5
	fig, ax = plt.subplots()
	
	indexes = np.arange(n_groups)
	bar_width = 0.1
	opacity = 0.4
	error_config = {'ecolor': '0.3'}
	
	# each sailor will have 6 bars because i am running 6 simulations - 6, 36, 180, 600, 2400, 9000 races...
	rects1 = ax.bar(indexes, scores[0], bar_width, alpha=opacity, color="b", error_kw=error_config, label="6 Races")
	
	rects2 = ax.bar(indexes+bar_width, scores[1], bar_width, alpha=opacity, color="g", error_kw=error_config, label="36 Races")
	
	rects3 = ax.bar(indexes+bar_width*2, scores[2], bar_width, alpha=opacity, color="r", error_kw=error_config, label="180 Races")
	
	rects4 = ax.bar(indexes+bar_width*3, scores[3], bar_width, alpha=opacity, color="c", error_kw=error_config, label="600 Races")
	
	rects5 = ax.bar(indexes+bar_width*4, scores[4], bar_width, alpha=opacity, color="m", error_kw=error_config, label="2400 Races")
	
	rects6 = ax.bar(indexes+bar_width*5, scores[5], bar_width, alpha=opacity, color="y", error_kw=error_config, label="9000 Races")
	
	# Customizing the appearance of the graph
	plt.ylabel("Average random performance scores")
	plt.xlabel("Sailors")
	plt.suptitle(title) 
	ax.set_xticks(indexes + bar_width*2)
	ax.set_xticklabels(["Alice", "Bob", "Clare", "Dennis", "Eva"])
	ax.set_ylim([0,130])

	plt.legend()
	plt.show()
	

# Each simulation will run over a different number of races
# First simulation only consists of 6, second simulation consists of 36 and so on..
raceNumbers = [6, 36, 180, 600, 2400, 9000]

# We get the average performance score for each sailor, rount it to a whole number and put them in a list for each sailor
# so scores below is a list of lists of the sailors' mean performance score
# the first score in every list refers to each sailor's result in the first simulation - a set of 6 races
# the second score in every list refers to each sailor's result in the second simulation - a set of 36 races and so on..
scores = calculateAverageScores(raceNumbers, True) # this will return something like this when we only one graph - simulations with worst score discarded
# [[[100, 99, 94, 90, 88], [100, 101, 105, 90, 89], [100, 99, 99, 90, 90], [100, 100, 99, 90, 89], [100, 99, 100, 90, 90], [100, 100, 99, 90, 90]]]
# We can also produce 3 different graphs with the same performance scores but with 2 worst scores discarded and no worst score discarded
# in that case we need to pass True as the second argument when we call calculateAverageScores
# if we pass True, then we will get a 3 dimensional list, where each graph will have a list of lists of average performance scores

# we will either have one graph with worst score discarded or 3 graphs with 1/0/2 worst scores discarded
for index in range(0, len(scores)):
	if index == 0:
		drawGraph(scores[index], "Average random performance scores against number of races\nWorst race is discarded")
	elif index == 1:
		drawGraph(scores[index], "Average random performance scores against number of races\nNo races are discarded")
	else:
		drawGraph(scores[index], "Average random performance scores against number of racesn\nWorst 2 races are discarded")


