def analyze_expenses(expenses):
    
    """
    Принимает список расходов и возвращает:
    total (float), average (float), max (float), min (float)
    """
     
    if not expenses:
        return 0, 0, None, None
    
    total = sum(expenses)
    average = total / len(expenses)
    mx = max(expenses)
    mn = min(expenses)
    return total, average, mx, mn
    

expenses = [12.5, 3.0, 18.9, 7.5, 22.0, 5.5]
total, avg, mx, mn = analyze_expenses(expenses)
print(f"Total: {total:.2f}")
print(f"Average: {avg:.2f}")
print(f"Max: {mx}")
print(f"Min: {mn}")


def filter_above_100(numbers):
    large_numbers = [x for x in numbers if x>100]
    return large_numbers

numbers = [50, 200, 30, 150]
result1 = filter_above_100(numbers)
print(f"numbers above 100 {result1}")

def filter_range(numbers, low, high):
    filtered = sorted(numbers)
    nums = [x for x in filtered if low <= x <= high]
    return nums
numbers = [10, 50, 120, 200, 300]

print(filter_range(numbers, 50, 200))


def filter_negative(numbers):
    return [x for x in numbers if x < 0]

print(filter_negative([10, -5, 0, -2, 8]))

def summary(numbers):
    if not numbers:
        return None
    return min(numbers), max(numbers), sum(numbers), sum(numbers)/len(numbers)
numbers = [10, -5, 0, -2, 8]

print(summary(numbers))

def filter_range(nums, low=0, high=100):
    return [x for x in nums if low <= x <=high]

nums = [10, -5, 0, -2, 8]

print(filter_range(nums, low=0, high=100))

def format_name(first, last):
    return f"{last}, {first}"

print(format_name("Rustam", "Saidazov"))

def top_product(products):
    mx = max(products.values())
    for k, v in products.items():
        if v == mx:
            return k
products = {
    "Apple": 120,
    "Banana": 60,
    "Orange": 90,
    "Mango": 30
}

print(top_product(products))

def greet(name, city="Chicago"):
    return f"Hello {name} from {city} "

print(greet("Rustam"))
print(greet("Rustam", city="NY"))


def convert_usd_to_eur(amounts, rate):
    return [round(x * rate, 2) for x in amounts]
print(convert_usd_to_eur([10, 20, 50], 0.92))