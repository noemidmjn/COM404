# read in two numbers from the user
print("Please enter first number")
number_one = float(input())

print("Please enter second number")
number_two = float(input())

if (number_one > number_two):
  print("\nThe first number is bigger!")
elif (number_one < number_two):
  print("\nThe second number is bigger!")
elif( number_one == number_two):
  print("\nBoth are equal!")
