from simplecrypt import encrypt, decrypt
import base64
import random
from Account import *
import sys

def welcome():
	print("Welcome to Cardiff ATM!")
	print("1. Login into your account")
	print("2. Create new account ")
	print("3. Exit")
	answer = input("- ")
	print()
	try:
		if int(answer) == 1:
			loginAccount()
		elif int(answer) == 2:
			print("Let's create a new account for you. Please enter your password!")
			createAccount()
		elif int(answer) == 3:
			print("Goodbye!")
			sys.exit()
		else:
			welcome()
	except ValueError:
		welcome()
		
def createAccount():
	answer = input("- ")
	if len(answer) >= 6:
		# save card number, 0 balance, enrypted password
		encryptedPassword = encrypt(answer, answer)
		cardNumber = random.randint(1000000,9999999)
		with open("accounts.txt", "a") as fileObjc:
			fileObjc.write(str(cardNumber) + " " + str(base64.b64encode(encryptedPassword),'utf-8') + " " + "0\n")
		account = Account(str(cardNumber), 0)
		mainMenu(account)
	else:
		print("Your password must have at least 6 characters")
		createAccount()
	

def loginAccount():
	print("Enter your card number!")
	cardNumber = input("- ")
	print("Enter your password")
	password = input("- ")
	found = False
	balance = 0
	
	with open("accounts.txt") as fileObjc:
		for line in fileObjc.readlines():
			line = line.split()
			if line[0] == cardNumber:
				try:
					decryptedPassword = decrypt(password, base64.b64decode(line[1])).decode("utf8")
				except:
					print("Incorrect password! Try again!")
					loginAccount()
					
				if decryptedPassword == password:
					print("You logged in successfully!\n")
					found = True
					balance = int(line[2])
					account = Account(line[0], balance)
					mainMenu(account)
					break
				else:
					break
					
	if found == False:
		print("Authenticatin failed!")
		print()
		welcome()
			
			
def mainMenu(account):
	print("Main menu")
	print("1. Check balance")	
	print("2. Deposit")
	print("3. Withdrawal")
	print("4. Send money")
	print("5. Lottery")
	print("6. Exit")
	answer = input("- ")
	print()
	try:
		if int(answer) == 1:
			checkBalance(account)
		elif int(answer) == 2:
			deposit(account)
		elif int(answer) == 3:
			withdrawal(account)
		elif int(answer) == 4:
			sendMoney(account)
		elif int(answer) == 5:
			lottery(account)
		elif int(answer) == 6:
			sys.exit()
		else:
			mainMenu(account)
	except ValueError:
		mainMenu(account)
		
def updateDatabase(account):
	newFileLines = []	

	with open("accounts.txt", "r") as fileObjc:
		lines = fileObjc.readlines()
		for index, item in enumerate(lines):
			data = item.split()
			if data[0] == account.cardNumber:
				data[2] = str(account.balance) + "\n"
				lines[index] = " ".join(data)
				break
		newFileLines = lines
	
	with open("accounts.txt", "w") as fileObjc:
		for each in newFileLines:
			fileObjc.write(each)
		
	
	
		
def checkBalance(account):
	print("Your account has $" + str(account.balance))
	print()
	mainMenu(account)
	
def deposit(account):
	print("Enter the amount for deposit!")
	try:
		amount = int(input("- "))
		print()
		account.addBalance(amount)
		updateDatabase(account)
		mainMenu(account)
	except ValueError:
		deposit(account)
	

def withdrawal(account):
	print("Enter the amount for withdrawal!")
	try:
		amount = int(input("- "))
		if account.balance - amount < 0:
			print("The maximum you can withdraw is $" + str(abs(0-account.balance)))
			withdrawal(account)
		print()
		account.subtractBalance(amount)
		updateDatabase(account)
		mainMenu(account)
	except ValueError:
		withdrawal(account)

def sendMoney(account):
	print("Enter the amount for transfer")
	try:
		amount = int(input("- "))
		if account.balance - amount < 0:
			print("The maximum you can withdraw is $" + str(abs(0-account.balance)))
			sendMoney(account)
			
		print("\nEnter the card number of the recipient")
		cardNumber = input("- ")
		found = False
		with open("accounts.txt") as fileObjc:
			for each in fileObjc.readlines():
				data = each.split()
				if data[0] == cardNumber:
					found = True
					recipient = Account(cardNumber, int(data[2]))
					recipient.addBalance(amount)
					account.subtractBalance(amount)
					updateDatabase(recipient)
					updateDatabase(account)
					print("Transfer success!\n")
					mainMenu(account)
					break
		
		if found == False:
			print("Recipient not found in the database!")
			sendMoney(account)
	except:
		sendMoney(account)

def lottery(account):
	print("Welcome to Lottery! Choose a ticket!")
	print("1. $10: Maximum win is $1,000")
	print("2. $20: Maximum win is $20,000")
	print("3. $50: Maximum win is $100,000")
	print("4. Main menu")
	
	try:
		answer = int(input("- "))
		if answer == 1:
			if account.balance - 10 < 0:
				print("You don't have enough money to buy this ticket!")
				mainMenu(account)
			else:
				account.subtractBalance(10)
				randomNumber1 = random.randint(0,20)
				randomNumber2 = random.randint(0,20)
				if randomNumber1 == randomNumber2:
					print("CONGRATS YOU WON $1,000")
					account.addBalance(1000)
					updateDatabase(account)
					print()
					mainMenu(account)
				else:
					print("Sorry you didn't win!")
					updateDatabase(account)
					print()
					mainMenu(account)
		elif answer == 2:
			if account.balance - 20 < 0:
				print("You don't have enough money to buy this ticket!")
				mainMenu(account)
			else:
				account.subtractBalance(20)
				randomNumber1 = random.randint(0,30)
				randomNumber2 = random.randint(0,30)
				if randomNumber1 == randomNumber2:
					print("CONGRATS YOU WON $20,000")
					account.addBalance(20000)
					updateDatabase(account)
					print()
					mainMenu(account)
				else:
					print("Sorry you didn't win!")
					updateDatabase(account)
					print()
					mainMenu(account)
		elif answer == 3:
			if account.balance - 50 < 0:
				print("You don't have enough money to buy this ticket!")
				mainMenu(account)
			else:
				account.subtractBalance(50)
				randomNumber1 = random.randint(0,1)
				randomNumber2 = random.randint(0,1)
				if randomNumber1 == randomNumber2:
					print("CONGRATS YOU WON $100,000")
					account.addBalance(100000)
					updateDatabase(account)
					print()
					mainMenu(account)
				else:
					print("Sorry you didn't win!")
					updateDatabase(account)
					print()
					mainMenu(account)
		elif answer == 4:
			mainMenu(account)
	except ValueError:
		lottery(account)


welcome()
