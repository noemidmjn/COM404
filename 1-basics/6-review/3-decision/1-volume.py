#
import math

print("Which shape would you like to calculate the volume for?")
print(" 1) cylinder")
print(" 2) cone")

response = int( input() )

print("Please enter the radius of the shape")
r = float( input() )

print("Please enter the hight of the shape")
h = float( input() )

cylinder = ( math.pi * (r ** 2) * h )

cone = (math.pi * (r ** 2) * h) / 3 

if (response == 1):
  print("Cylinder volume is", round(cylinder, 2))
elif (response == 2):
  print("Cone volume is", round(cone, 2))
else:
  print("I don't know that shape")
