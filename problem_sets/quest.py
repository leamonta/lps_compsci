	
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

direction = raw_input()
if direction == "right" and strength <= 8:
        print("Sorry, your character's strength was too low to get pass the fork and fell in a lake and drowned :(, you lost")

if direction == "right" and strength > 8:
        print("Yay!!!, you are a strong person to get pass the fork and walked home safely :), you won")

if direction == "left" and health <= 8:
        print("You tried to get over the fork, but died and while doing it because you health was too low, you lost")

if direction == "left" and health > 8:
	print("Yayy!!!, Now a bird pick you up and flew you home and be safe because your health was high enough to get over the fork, you won")
