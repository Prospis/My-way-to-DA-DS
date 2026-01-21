sales = {
    "Apple": 120,
    "Banana": 120,
    "Orange": 90,
    "Mango": 30,
    "Grapes": 55
}
total_sales = sum(sales.values())
filtered = [key for key,val in sales.items() if val > 50]
mx = max(sales.values())
top_product = [key for key,val in sales.items() if val == mx]
print(f"Total sales: {total_sales:.2f}")
print(f"Filtered (>50): {filtered}")
print(f"Top product: {top_product} ({mx} units) ")