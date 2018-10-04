# read in current amount from user
print("Enter current amount of savings")

current_amount = float( input() )

print("\nEnter the percentage interest rate (%)")

interest_rate = float( input() )

interest_amount = (interest_rate / 100) * current_amount
new_amount = current_amount + interest_amount
print("\nYour new amount is Ł", str( round(new_amount, 2)))
