print("I'm thinking of a number between 1 and 1000.  Enter your guess!:")
import random 
myNum = random.randint(1, 1000)
x = 0
x = int(raw_input())

while x != myNum:
	if  x > myNum:
		print("Nope, too high!")
		x = int(raw_input())	
 		if x == myNum:
			print("Hooray, you won!")
	if x < myNum:
		print("Nope, too low!")
		x = int(raw_input())
		if x == myNum:
			print("Hooray, you won!")
