count_of_categories = int(input(f"How many categories do you have today?"))
categories = {}
count_of_expence = []
for i in range(count_of_categories):
    category_name = input(f"Enter the name of category {i +1}  ")
    category_count = int(input(f"How many expenses in this category?  "))
    category_expence = []
    count_of_expence.append(category_count)
    for j in range(category_count):
        amount = float(input(f"Enter expense ... {j+1}  "))
        category_expence.append(amount)    
    categories[category_name] = category_expence   
total_expenses = sum(sum(amounts) for amounts in categories.values()) 
all_expenses = [amount for amounts in categories.values() for amount in amounts]
mx = max(all_expenses)
mn = min(all_expenses)
print(categories)
print(f"You total expenses: {total_expenses:.2f}")
print(f"Average expense: {total_expenses/sum(count_of_expence):.2f}")
print(f"Max expense: {mx:.2f}")
print(f"Min expense: {mn:.2f}")
print(f"Count of expenses: {sum(count_of_expence)}")