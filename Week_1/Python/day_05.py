

def analyze_payroll(data):
    good_salaries = [] # Сюда будем складывать только правильные цифры
    
    for i in data:
        if i <= 0:
            print(f"Ошибка! Найден подозрительный чек: {i}")
        else:
            good_salaries.append(i) # Добавляем только положительные числа
            
    # Проверка на случай, если список окажется пустым, чтобы не делить на ноль
    if len(good_salaries) > 0:
        avg_data = sum(good_salaries) / len(good_salaries)
        return round(avg_data, 2)
    else:
        return "Нет корректных данных для расчета"

salaries = [4500, 5200, 3800, -1000, 6100, 0, 4900]

print(f"Средняя зарплата (после очистки): {analyze_payroll(salaries)}")

