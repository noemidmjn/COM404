print("Please enter a character to display...")
character = str(input())
print("Please enter total number of characters...")
total_n_of_characters = int(input())
print("Please enter a whole number...")
whole_number = int(input())

for count in range (1, total_n_of_characters + 1, 1):
  if (count % whole_number == 0):
    print(character, end = "")
  else: 
    print("-", end = "")
    
