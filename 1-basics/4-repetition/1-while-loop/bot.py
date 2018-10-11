#
print("How many ascii robots sould I draw?")
robot_num = int(input())
count = 0
print("Here I go:")

if robot_num < 10:
  while count < robot_num:
      print("#########")
      print("#       #")
      print("# O   O #")
      print("|   V   |")
      print("|  ---  |")
      print("|_______|")
      count += 1

else:
  while count <= 10:
    print("#########")
    print("#       #")
    print("# O   O #")
    print("|   V   |")
    print("|  ---  |")
    print("|_______|")
    count += 1
