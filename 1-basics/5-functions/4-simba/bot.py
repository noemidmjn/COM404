def roar(num_roars):

  print("\n Simba says:")
  
  for count in range(0, num_roars, 1):
    print("roar")

  if (num_roars < 3):
    print("cough! cough!")
  else:
    print("ROAR!!!")

  
# The following are calls to the function for testing purposes
roar(1)
roar(3)

roar(5)
roar(9)
