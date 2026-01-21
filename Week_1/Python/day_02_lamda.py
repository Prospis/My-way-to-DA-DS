sales = {
    "Apple": 120,
    "Banana": 60,
    "Orange": 90,
    "Mango": 30,
    "Grapes": 55
}
pairs = list(sales.items()) 
sorted_pairs=sorted(pairs, key=lambda x: x[1], reverse=True)
top3 = sorted_pairs[:3]
top3_names = [i[0] for i in top3]

print(f"Sorted: {sorted_pairs}")
print(f"Вывести топ-3 продукта {top3_names}")