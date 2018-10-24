# practice paper q7

print("Please enter a word")
word = str(input())

def under():
  print(word)
  print((len(word)) * "*")

def over():
  print((len(word)) * "*")
  print(word)

def both():
  print((len(word)) * "*")
  print(word)
  print((len(word)) * "*")

def grid():
  print("Give me a whole number")
  number = int(input())
  for x in range(number):
    print((len(word)) * "*" * number)
    print(word  * number)
    print((len(word) ) * "*" * number)
  


def run():
  print("Choose")
  response = str(input())
  if (response == "under"):
    under()
  elif (response == "over"):
    over()
  elif (response == "both"):
    both()
  elif (response == "grid"):
    grid()

run()
