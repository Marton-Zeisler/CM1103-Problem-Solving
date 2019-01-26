# files and exceptions


with open("colors.txt", "a") as fileObj:
	fileObj.write("\ngrey\n")
	fileObj.write("orange")

with open("colors.txt") as fileObj:
	for line in fileObj.readlines():
		line = line.rstrip()
		print(line)
		
