import random

print("Quick Math Test")

num1 = random.randint(1,100)
num2 = random.randint(1,100)

print("What is " + str(num1)+ " + " + str(num2)+" = ?")

user = int(input())

userIsCorrect = user == num1 + num2

if userIsCorrect:
  print("Good Job")
else:
  print("Not Correct!")

#while user is not correct
while (not userIsCorrect):
  num1 = random.randint(1,100)
  num2 = random.randint(1,100)

  print("What is " + str(num1)+ " + " + str(num2)+" = ?")

  user = int(input())

  userIsCorrect = user == num1 + num2

  if userIsCorrect:
    print("Good Job")
  else:
    print("Not Correct!")


print("Congradulations!!!!")
