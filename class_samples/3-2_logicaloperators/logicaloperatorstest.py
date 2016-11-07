# number 2

#This print statement is going to ask us our age
print("How old are you?")
#the age is the variable assigned to an integer witch we have to enter our age
age = int(input())

#this print statement is going to ask us our height in inches
print("How many inches tall are you?")
#the height is the variable assigned to an integer witch we have to enter our height
height = int(input())

#If age greater than 10 and height greater than 50 I can ride or less than, I can't
if age > 10 and height > 50:
	print("Hooray! You're old enough and tall enough to ride.")
else:
	print("Sorry, you can't ride.")
