transactions = [120, -50, -20, 300, -100, 50]
spent = [x for x in transactions if x<0]
income = [i for i in transactions if i>0]

print(f"Total: {sum(transactions):.2f}")
print(f"Incomes: {sum(income):.2f} (count: {len(income)})")
print(f"Expenses: {sum(spent):.2f} (count: {len(spent)})")
print()