#ask the user for data name age weight height

print("Please enter your name")
name = str(input())

print("Please enter your age")
age = int(input())

print("Plase enter your weight")
weight = float(input())

print("Please enter your height")
height = float(input())

bmi = weight / (height * height)
print(name, "your BMI is", bmi, "and you are", age, "years old")
