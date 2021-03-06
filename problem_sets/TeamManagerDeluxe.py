# It will call the object and have the classes below
class Players(object): 
  """ Encapsulates the name, age, goals,jersey number, and position """

  # The function, __init__ will call and define the classes below to self
  def __init__(self, name, age, goals, jerseynumber, position):
    self.name = name
    self.age = age
    self.goals = goals
    self.jerseynumber = jerseynumber
    self.position = position

  # This function will give us the summary back of the person name they entered, age and number of goals   
  def getStats(self):
    summary = 'Name: ' + self.name + '\n'
    summary = summary + 'Age: ' + str(self.age) + '\n'
    summary = summary + 'Goals: ' + str(self.goals) + '\n'
    summary = summary + 'Jersey Number: ' + str(self.jerseynumber) + '\n'
    summary = summary + 'Position: ' + str(self.position) + '\n'
    return summary




# This is an empty list because the user needs to make their own list of their players and keep it stored when print    
print('Welcome to Team Manager Deluxe!')
print('Do you want to start with a new team or open an exsiting team?')
print('Enter your choice and press Enter')
print('(1) Start with a new team')
print('(2) Open a file for an existing team')


#save the team in the file
def saveTeam(playerList, filename):
	myFile = open(filename , 'r')
	myFile.close()
	pass


#load the team in the file
def loadTeam(myPlayers):
	print('What is the filename for your existing team? Enter the whole name, including its .tmd extension')
 	filechoice = raw_input()
	team = []
        myFile = open('pumas.tmd' , 'r')
        line = myFile.readline()
        while line != "":
        	splitter = line.split()
                line = myFile.readline()
        myFile.close()
	return myPlayers


myPlayers = []
    
# When the program is true, it will run and print out the options
	
choose = raw_input()
	
if choose == '1':
	print('Enter their name: ')
        playerName = raw_input()
        print('Enter their age: ')
	playerAge = raw_input()
       	print('Enter their number of goals: ')
        playerGoals = raw_input()
        print('Enter their jersey number: ')
        playerJerseyNumber = raw_input()
        print('Enter their position: ')
        playerPosition = raw_input()

	myPlayers.append(Players(playerName, playerAge, playerGoals, playerJerseyNumber, playerPosition))

	

if choose == '2':
	myPlayers = loadTeam(myPlayers)
			

program = True
while program == True:

	print('What would you like to do? Enter your choice.')
	print('(1) Add players')
	print('(2) Print all players')
	print('(3) Save your player list to a file')
	print('(0) Exit and delete the info')
      	
        # This way you can input the choice you want
      	choice = raw_input()

        # If you input 0, the program will stop running,  exit you out & delete the info you entered. 
	if choice == '0':
		program = False 
        # If you input 1, the program will ask you input a name, age and goals
	if choice == '1':
		print('Enter their name: ')
       	 	playerName = raw_input()
       	 	print('Enter their age: ')
       	 	playerAge = raw_input()
       	 	print('Enter their number of goals: ')
       	 	playerGoals = raw_input()
		print('Enter their jersey number: ')
		playerJerseyNumber = raw_input()
		print('Enter their position: ')
		playerPosition = raw_input()
        
		myPlayers.append(Players(playerName, playerAge, playerGoals, playerJerseyNumber, playerPosition))

        # If you input 2, the program will print the player(s) that you've entered with their name, age & goals
	if choice == '2':
        
		for p in myPlayers:
		 	print(p.getStats())

      	if choice == '3':
		myPlayers = saveTeam(myPlayers, 'pumas.tmd')
			
		

