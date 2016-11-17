months = 0
ticket = 60

while ticket > 0:
	print("Did you pay your ticket")
	response = raw_input()
	if response == "yes":
		ticket = 0
	else: 
		ticket = ticket * 2
	print("Ok, your ticket is now " + str(ticket))
