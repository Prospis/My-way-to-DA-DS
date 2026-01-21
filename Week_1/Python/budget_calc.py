total_budget = 1500
total_spent = float(input("How much have you spent today? "))

remaining = total_budget - total_spent
print(f"You have spent ${total_spent:.2f} today.")
print(f"Remaining monthly budget: ${remaining:.2f}")
if total_spent > 100:
    print("Warning: heavy spending day!")
else:
    print("Spending is under control.")