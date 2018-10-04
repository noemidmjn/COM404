# read 3 number from user
print("Please enter a number:")
number_one = int( input() )

print("Please enter a number")
number_two = int( input() )

print("Please enter a number")
number_three = int( input() )

# work out which number are even and odd
evens = 0
odds = 0

if (number_one % 2 == 0):
  evens = evens + 1
else:
  odds = odds + 1

if (number_two % 2 == 0):
  evens = evens + 1
else: 
  odds = odds + 1

if (number_three % 2 == 0):
  evens = evens + 1
else: 
  odds = odds + 1

print("The total number of evens is", evens)
print("The total number of odds is", odds)
