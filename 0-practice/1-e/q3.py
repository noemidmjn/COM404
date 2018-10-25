# practice paper q3
print("How many zones must I cross?")
zones = int(input())
print("Crossing zones...")
while (zones > 0):
  print("...crossed zone", zones)
  zones = zones - 1
  if zones == 0:
    print("Crossed all zones.  Jumanji!")

    
    
    
    print("How many zones must I cross?")

zones = int(input())

print("Crossing zones...")

for count in range (zones, 0, -1):
  print("...crossing zones", zones)
