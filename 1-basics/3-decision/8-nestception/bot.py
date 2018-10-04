# ask user where to look and read user's respond
# choices are as follows:
# 1) in the bedroom
# 2) in the bathroom
# 3) in the lab
# 4) somwhere else

# in the bedroom
# ask the user where in the bedroom
# choices are as follows:
# 1) under the bed
# found some socks but no battery
# 2) somwhere else
# found mess but no battery

# in the bathroom
# ask where in the bathroom
# 1) in the bathtub
#  found a rubber duck but no battery
# 2)somewhere else
#  it's wet but no battery

# in the lab
# ask where
# 1) on the table
#  found the battery
# 2) somwhere else
#  found some tools but no battery 

print("Where can I find new battery?")
print("1) in the bedroom")
print("2) in the bathroom")
print("3) int the lab")

place = int(input())
if (place == 1):
  print("\nWhere in the bedroom?")
  print("1) under the bed")
  print("2) somwhere else")

  bedroom_place = int( input() )
  if (bedroom_place == 1):
    print("\nFound some socks but no battery")
  else:
    print("\nFound mess but no battery")

elif (place == 2):
  print("Where in the bathroom?")
  print("1) In the bathtub")
  print("2) Somwhere else")
  bathroom_place = int( input() )
  if (bathroom_place == 1):
    print("Found a rubber duck but no battery")
  else:
    print("It's wet but no battery")

elif (place == 3):
  print("Where in the lab?")
  print("1) on the table")
  print("2) somwhere else")
  bathroom_place = int( input() )
  if (bathroom_place == 1):
    print("I found battery")
  else:
    print("Found some tools but no battery")
  
else:
  print("Not sure where that is but I will keep looking.")
