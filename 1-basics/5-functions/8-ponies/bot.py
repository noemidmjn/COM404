def sum_ages_of_friends(age_1, age_2, age_3):
  total = age_1 + age_2 + age_3
  return total

def calc_avg_age_of_friends(age_1, age_2, age_3):
  total = age_1 + age_2 + age_3
  avg = total / 3
  return avg

def run():
  print("Please enter the ages of the three friends")
  age_1 = int(input())
  age_2 = int(input())
  age_3 = int(input())
  print("Do you want to know the sum or the average?")
  ans = str(input())

  if (ans == "sum"):
    print(sum_ages_of_friends(age_1, age_2, age_3))
  elif (ans == "average"):
    print(calc_avg_age_of_friends(age_1, age_2, age_3))
  else:
    print("error")

run()
