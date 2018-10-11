#
print("How many ascii robots sould I draw?")
robot_num = int(input())
print("Here I go:")

if robot_num < 10:
  for count in range(0, robot_num, 1):
    print("#########")
    print("#       #")
    print("# O   O #")
    print("|   V   |")
    print("|  ---  |")
    print("|_______|")
else:
  if robot_num > 10:
    for count in range(10):
        print("#########")
        print("#       #")
        print("# O   O #")
        print("|   V   |")
        print("|  ---  |")
        print("|_______|")
