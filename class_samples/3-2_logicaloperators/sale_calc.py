print("What is the amount that you purchase?")
cents = int(raw_input())

if cents > 1000:
	print("You get the discount")
if cents < 1000:
	print("You do not get the discount") 

