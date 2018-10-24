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
  


def run():
  print("Choose")
  response = str(input())
  if (response == "under"):
    under()
  elif (response == "over"):
    over()
  elif (response == "both"):
    both()

run()
