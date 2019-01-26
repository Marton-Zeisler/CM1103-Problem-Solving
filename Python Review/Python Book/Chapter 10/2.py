try:
	print(5/0)
except ZeroDivisionError:
	print("can't divide by 0 you shit")
except:
	print("error")
	

try:
	with open("colors.txt") as fileObj:
		print(fileObj.readlines())
except FileNotFoundError:
	pass
except:
	print("other error")