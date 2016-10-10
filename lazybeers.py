#Imports the time library  for the sleep function I use on likes 8, 12 and 15
import time

#Declares the X variable
x = 99


#Loops until x = 0
while x != 0:

	#Turns x into a string so it can be added to other strings without type errors
	xs = str(x)
	
	#Prints the first line
	print(xs + " Bottles of beer on the wall")

	#sleeps so that user has time to read the output
	time.sleep(.2)

	#Prints the second line
	print(xs + " Bottles of beer")
	
	#Takes 1 away from x 
	y = x-1

	#Turns y into a string so it can be added to other strings without type errors
	ys = str(y)

	#sleeps so that user has time to read the output
	time.sleep(.2)

	#Prints the third line
	print("Take one down pass it around you have " + ys + " Bottles of beer on the wall")
	
	#sets x to be equal to y
	x = y

	#sleeps so that user has time to read the output
	time.sleep(.5)