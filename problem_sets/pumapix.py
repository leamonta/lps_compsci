# This is just print statements that welcoming the user into the program and to input 5 TV shows
print("Welcome to PumaPix!")
print("Enter your 5 favorite TV shows.")
# The variable(numbers) is assigned to the interger, 0
numbers = int(0)
# The variable(choices) is assigned to empty list so it can print out what the user input
choices = []
# This is a while statement so that the user can exactly only input 5 TV shows 
while numbers < 5:
	print("Enter a show name:")
	new_choice = raw_input()
	choices.append(new_choice)
	numbers = numbers + 1
# These are print statements so the user can see what they have entered afterwards	
print("Ok, here's what you entered:")
print(choices)
# This is a new variable(new_shows) assigned to the new list of TV shows that I want to add to the user list of Tv shows	
new_shows = ["Breaking Bad" , "The Wire"]
# This is a variable(list) that is assigned to the choices that the user input and the new shows above that will add the two lists together 
list = choices + new_shows 
# This is the variable(numbers) that assigned to the integer, 0 so that it can number the shows this program will have
numbers = 0
# This will print out the user inputs with the new_shows shows in alphabetical order  
print("We have added couple of new shows:")
list.sort()
print(list)
# This is a for statement so that it can number the shows from 1-7 
for show in list:
	numbers = numbers + 1
	print(str(numbers) + "." + show)





	
