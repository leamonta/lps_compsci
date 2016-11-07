print("How many miles do you live from Richmond State?")
miles = int(input())

print("What is your GPA?")
GPA = float(input())

print("What is your ACT score?")
ACT = int(input())

if miles <= 30 and GPA >= 2.0:
	print("You been accepted to Richmond State")
elif miles < 30 and GPA < 2.0: 
	print("Sorry, you are not accepted")

if miles > 30 and GPA > 2.5 and ACT >= 18: 
	print("You been accepted to Richmond State")
elif miles > 30 and GPA < 2.5 and ACT >= 18:
	print("Sorry, you are not accepted")

elif miles > 30 and GPA > 2.5 and ACT >= 18:
	print("Sorry, you are not accepted")

elif miles > 30 and GPA > 2.5 and ACT >= 18:
	print("You have been accepted to Richmond State") 


