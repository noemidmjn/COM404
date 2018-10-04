#
print("Please enter a direction from the following:")
print("...w to move up")
print("...s to move down")
print("...a to move left")
print("...d to move right")

direction = str( input() )

if (direction == "w"):
  print("The character is moving up")

elif (direction == "s"):
  print("The character is moving down")

elif (direction == "a"):
  print("The character is moving left")

elif (direction == "d"):
  print("The character is moving right")

else:
  print("I'm not sure what direction it is")
