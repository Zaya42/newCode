"""import random

rand = random.randint(1,100)

if rand > 50:
  print("isaiah")

  
else: # rand <= 50
  print("skyy")"""

import random

print("Quick Math Test")

num1 = random.randint(1,100)
num2 = random.randint(1,100)

print("What is " + str(num1)+ " + " + str(num2)+" = ?")

user = int(input())

if user == num1 + num2:
  print("Good Job")
else:
  print("Not Correct!")


