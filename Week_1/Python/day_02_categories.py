numbers_of_categories = int(input("How many expense categories do you have today? "))
categories = {} 
for i in range(numbers_of_categories):
    category_name = input(f"Enter the name of category {i+1}: ")
    category_count = int(input(f"How many expenses in {category_name}? "))
    category_expenses = []
    for j in range(category_count):
        amount = float(input(f"Enter expense {j+1} for {category_name}: "))
        category_expenses.append(amount)
    categories[category_name] = category_expenses
total_expenses = sum(sum(amounts) for amounts in categories.values())

print(categories)
print(f"Today's total expenses across all categories: {total_expenses:.2f}")
