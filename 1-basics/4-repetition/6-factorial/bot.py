# calculate and display the factorial of a number specified by the user
print("please enter a number")
number = int(input())
total = 1
for count in range(1, number + 1):
  total = total * count


print("The factorial of your number is", total)
