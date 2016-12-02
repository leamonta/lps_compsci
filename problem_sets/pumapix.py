print("Welcome to PumaPix!")
print("Enter your 5 favorite TV shows.")
numbers = int(0)
while numbers < 5:
	print("Enter a show name:")
	choice = [raw_input()]
	numbers = numbers + 1
	print("Ok, here's what you entered:" + str(choice) + ".")
		
new_shows = ["Breaking Bad" , "The Wire"]
another = choice + new_shows
for show in new_shows:
	numbers = numbers + 1
	print(str(numbers) + " " + show)
another.sort()
print(another)

	
