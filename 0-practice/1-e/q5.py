# practice paper q5

health = 100
print("Your health is 100%. Escape is in progress...")

# counting, starting at 1, finish at 5
for count in range (1, 6, 1):
  print("\n…Oh dear, who is that?")
  answer = str(input())
  if (answer == "Smiler's Bot"):
    # substract 20 from the value of health
    health = health - 20
    print("Time to jam out of here!")
  elif (answer == "Hacker"):
    # adding 20 to the value of health
    health = health + 20
    print("Yay! Better follow this one!")
  else:
    print("Phew, just another emoji!")
    
# displaying health in %
print("\nEscaped! Health is", health,"%")
