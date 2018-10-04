# read radius from user
import math

print("Please enter radius")
radius = float( input () )
area = math.pi * (radius * radius)
# area = math.pi = (radius ** 2)
#area = math.pi * pow(radius, 2)

circumference = 2 * math.pi * radius
print("\nArea is", area)
print("Circumference is", circumference)
