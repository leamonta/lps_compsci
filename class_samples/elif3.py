# number 1

# This print statement will ask us to input our age
print("Hi! How old are you?")
# Age is assigned to a integer 
age = int(input())

# this if statement is saying that if the age is greater or equal to 18, I am too old to use swingset
if age >= 18:
  print("Sorry, you're too old to use the swingset!")
# this is something else, if age is less that 5, I can use the babd swings
else:
  if age < 5:
    print("Welcome to the park! Use the baby swings.")
# it is the opposite of the else statement, if age is less than 10 before 5, I can use the big swings
  elif age < 10:
    print("Welcome to the park! Use the big swings.")
# this is something else, it is the opposite
  else:
    print("Welcome to the park! Push a little kid on the swings.")
