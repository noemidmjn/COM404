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
  elif (bedroom_place == 2):
    print("\nFound mess but no battery")
