count_of_expenses = int(input("Enter the number of expenses you have today: "))
expenses = []
for i in range(count_of_expenses):
    amount = float(input(f"Enter expense {i+1} "))
    expenses.append(amount) 

print(f"Today's expenses: {sum(expenses):.2f}")

monthly_budget = 1500
remaining = monthly_budget - sum(expenses)

print(f"Remaining monthly budget: ${remaining:.2f}")