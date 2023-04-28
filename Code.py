budget = float(input("What is your budget for the month? "))
print("Please begin entering the amounts of each of your monthly expenses:")

sum_of_expenses = 0
while True:
    expense = float(input("Monthly expense amount? $"))
    sum_of_expenses += expense
    continue_input = input("Do you have any other expenses? (Enter y for yes.) ")
    if continue_input.lower() != 'y':
        break

if sum_of_expenses < budget:
    difference = budget - sum_of_expenses
    print(f"You were ${difference:.2f} under budget.")
elif sum_of_expenses > budget:
    difference = sum_of_expenses - budget
    print(f"You were ${difference:.2f} over budget.")
else:
    print("You were right on budget. Great Job!!!")

input("Press enter to exit.")
