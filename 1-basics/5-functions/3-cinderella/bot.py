def try_glass_slipper_on(person):
  
  if (person.lower() == "cinderella"):
    print("I found my princess!")
  elif (person.lower() == "eldest step sister"):
    print("You are not my princess. Your feet are too big!")
  elif (person.lower() == "youngest step sister"):
    print("You are not my princess. Your feet are too small!")
  
# The following are calls to the function for testing purposes
try_glass_slipper_on("Eldest step sister")
try_glass_slipper_on("Youngest step sister")
try_glass_slipper_on("Cinderella")
