#
print("Please enter a sequence")
sequence = str(input())

print("Please enter the character for the marker")
marker = str(input())

first_marker_position = -1
second_marker_position = -1

for position in range(0, len(sequence), 1):
  letter = sequence[position]

  if (letter == marker):
    if (first_marker_position == -1):
      first_marker_position = position
    else:
      second_marker_position = position


print("The distance between the markers is", second_marker_position - first_marker_position - 1)
