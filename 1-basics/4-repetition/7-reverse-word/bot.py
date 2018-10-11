# display word in reverse
print("Give me a word")
word = str(input())

for position in range(len(word) - 1, -1, -1):
  print(word[position], end="")
