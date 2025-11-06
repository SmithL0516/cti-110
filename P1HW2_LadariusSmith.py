# Ladarius Smith
# 11/5/25
#P1HW2
# This program calculates and displays travel expenses


# calculate a budget

print("-------Travel Expenses-------")
print()

budget = float(input("Enter your budget: "))
destination = input("Enter a Travel destination: ")
gas = float(input("Enter a amount used for gas: "))
accommodation = float(input("Enter a amount used for accommodation: "))
food = float(input("Enter a amount used for food: "))

total_expenses = gas + accommodation + food
remaining_balance = budget - total_expenses

print("------------travel cost------------")
print("location:", destination)
print("available balance:", budget)
print()
print("fuel:", gas)
print("accommodation:", accommodation)
print("food:", food)
print()
print("total expenses:", total_expenses)
print("balance left over:", remaining_balance)