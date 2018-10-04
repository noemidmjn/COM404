# modulo operator (%) returns the remainder after division. 
# For example, 4 % 2 returns 0.
# 5 % 3 returns 2.
# If a number is even, it will have a remainder of 0 after dividing by 2.

#read whole number from user
print("Give me a whole number")
user_number = int( input() )

if (user_number % 2 == 0):
  print ("The number is even")
else:
  print("The number is odd")
