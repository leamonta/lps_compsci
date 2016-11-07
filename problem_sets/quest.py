print("Welcome to Leamonta's Quest!!")

print("Enter the name of your character:")
name = raw_input()

print("Enter strength (1-10):")
strength = int(raw_input())

print("Enter health (1-10):")
health = int(raw_input())

print("Enter luck (1-10):")
luck = int(raw_input())

if strength +  health + luck > 15: 
	print("You have give your character too many point! Default values have been assigned, strength: 5, Health: 5, Luck: 5") 
	strength = 5
	health = 5
	luck = 5

if strength + health + luck <= 15:
	print("Your character name is " + name + " and your strength is " + str(strength) + " and your health is " + str(health) + " and your luck is " + str(luck)) 

print("You've come to a fork in the road. Do you want to go right or left?")
choice = raw_input()
if choice == right and strength + health + luck > 8: 
	print("
