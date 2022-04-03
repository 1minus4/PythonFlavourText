# I'm dumb so this mess is needed in here to SUMMON THE ALMIGHTY ONE!!!
# ( someone please help, I have the coding skills of a cardboard box )

from libs import pyFlavText
import time

def MaximumFlava():
	# define parameters
	num1 = int(input("do:"))
	num2 = 0
	timeBetw = float(input("seconds between: "))
	# just empty space, don't worry about it
	print("")
	# loop to produce output desired no. of times
	while num2 < num1:
		output = pyFlavText.testingLOL()
		# strLenny = len(output)
		# for debugging purposes
		# print(strLenny) # ( ͡° ͜ʖ ͡°)
		num2+=1
		time.sleep(timeBetw)

MaximumFlava() 
