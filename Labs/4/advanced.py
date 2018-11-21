import csv
import re


def checkPost():
	with open("postcodes.txt") as csvfile:
		reader = csv.reader(csvfile)
		for each in reader:
			postCode = each[0]
			result = re.match("[A-Z]{2}[0-9]{1,2}[0-9][A-Z]{1,2}", postCode)
			if result:
				print("Matched!")
			else:
				print("Not Matched!")
			

checkPost()

