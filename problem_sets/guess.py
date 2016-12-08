# A print statement that ask the user to input of any number(1-1000)
print("I'm thinking of a number between 1 and 1000.  Enter your guess:")
# This will make the program randomly select a number between 1-1000
import random 
# The variable(myNum) is assigned to any random numbers 1-1000  
myNum = random.randint(1, 1000)
# The variable(x) is assined to integer 0 
x = 0
# The variable(x) is assigned to raw input so the user can input a number
x = int(raw_input())

# This while statement so it can repeat it over again when the person picks the wrong number so they can try again
while x != myNum:
	# If the user input is greater than the random number, it will print,"Nope, too high!" and user can pick a lower number than before
	if  x > myNum:
		print("Nope, too high!")
		# This is so that if they choose the wrong number, they can try again and again since it is in a while loop
		x = int(raw_input())	
		# If the user input chooses the correct random number, they win the game and the loop terminate
 		if x == myNum:
			print("You chose the right number, you won!")
	# If the user input is less than the random number, it will print,"Nope, too low!" and user can pick a higher number than before  	
	if x < myNum:
		print("Nope, too low!")
		# This is so that if they choose the wrong number, they can try again and again since it is in a while loop
		x = int(raw_input())
		# If the user input chooses the correct random number, they win the game and the loop terminate
		if x == myNum:
			print("You chose the right number, you won!")
