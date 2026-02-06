📊 PANDAS: Шпаргалка для Data Analyst
🔍 Обзор данных (Exploration)
Первый взгляд на данные
pythondf.head(10)          # Первые 10 строк
df.tail(5)           # Последние 5 строк
df.sample(10)        # 10 случайных строк
df.shape             # (строк, колонок) → (1000, 9)
df.columns           # Названия колонок
df.info()            # Типы данных + пропуски
df.describe()        # Статистика по числовым колонкам

🧹 Очистка данных (Cleaning)
Проверка пропусков
pythondf.isnull().sum()    # Количество пропусков в каждой колонке
df.dropna()          # Удалить строки с пропусками
df.fillna(0)         # Заполнить пропуски нулями
df.fillna(df['Age'].mean())  # Заполнить средним значением
Конвертация типов
python# Дата из текста в datetime
df['Date'] = pd.to_datetime(df['Date'])

# Число из текста
df['Price'] = pd.to_numeric(df['Price'])

# Категория (для экономии памяти)
df['Gender'] = df['Gender'].astype('category')
Работа с датами (после конвертации в datetime)
pythondf['Year'] = df['Date'].dt.year
df['Month'] = df['Date'].dt.month
df['Month_name'] = df['Date'].dt.month_name()
df['Day'] = df['Date'].dt.day
df['Day_name'] = df['Date'].dt.day_name()
df['Day_of_week'] = df['Date'].dt.dayofweek  # 0=Monday, 6=Sunday
df['Quarter'] = df['Date'].dt.quarter
Создание новых колонок
python# Простая формула
df['Total'] = df['Price'] * df['Quantity']

# Категоризация (разбивка на группы)
df['Age_Group'] = pd.cut(df['Age'], 
                         bins=[17, 30, 45, 65], 
                         labels=['Young', 'Middle', 'Senior'])

# Условие (if-else)
df['Expensive'] = df['Price'] > 100  # True/False

📊 Анализ данных (Analysis)
Базовые метрики
pythondf['Sales'].sum()      # Сумма
df['Age'].mean()       # Среднее
df['Price'].median()   # Медиана (50-й перцентиль)
df['Quantity'].min()   # Минимум
df['Quantity'].max()   # Максимум
df['Age'].std()        # Стандартное отклонение
df['Customer'].nunique()  # Количество уникальных значений
df['Category'].unique()   # Список уникальных значений
df['Gender'].value_counts()  # Подсчёт каждого значения
Группировка (КЛЮЧЕВОЙ НАВЫК!)
python# Базовый синтаксис
df.groupby('колонка')['что_считать'].функция()

# Примеры:
df.groupby('Category')['Sales'].sum()  # Выручка по категориям
df.groupby('Gender')['Age'].mean()     # Средний возраст М/Ж
df.groupby('Month')['ID'].count()      # Количество по месяцам

# Несколько функций сразу
df.groupby('Category')['Sales'].agg(['sum', 'mean', 'count'])

# Группировка по двум колонкам
df.groupby(['Category', 'Gender'])['Sales'].sum()
Сортировка
pythondf.sort_values('Sales', ascending=False)  # От большего к меньшему
df.sort_values('Age')                     # От меньшего к большему
df.sort_values(['Category', 'Price'])     # По двум колонкам
Фильтрация
python# Одно условие
df[df['Age'] > 40]
df[df['Category'] == 'Electronics']

# Два условия (И)
df[(df['Age'] > 40) & (df['Gender'] == 'Female')]

# Два условия (ИЛИ)
df[(df['Category'] == 'Beauty') | (df['Category'] == 'Clothing')]

# Несколько значений
df[df['Category'].isin(['Beauty', 'Electronics'])]

# НЕ равно
df[df['Gender'] != 'Male']
Топ N значений
pythondf.nlargest(10, 'Sales')   # Топ-10 по продажам
df.nsmallest(5, 'Price')   # 5 самых дешёвых

💾 Сохранение данных
python# CSV (самый популярный формат)
df.to_csv('clean_data.csv', index=False)

# Excel
df.to_excel('report.xlsx', index=False, sheet_name='Sales')

# Несколько листов в Excel
with pd.ExcelWriter('report.xlsx') as writer:
    df1.to_excel(writer, sheet_name='Sales', index=False)
    df2.to_excel(writer, sheet_name='Customers', index=False)

🎯 Когда что использовать?
ЗадачаМетодПонять структуру данных.info(), .head()Найти пропуски.isnull().sum()Посчитать общую выручку.sum()Средний чек.mean()Выручка по категориям.groupby().sum()Топ-10 клиентов.nlargest(10)Отфильтровать женщин 40+df[(df['Gender']=='Female') & (df['Age']>40)]Разбить возраст на группыpd.cut()

⚠️ Частые ошибки
❌ Неправильно:
pythondf['Date'].dt.month  # Ошибка, если Date — text (object)
✅ Правильно:
pythondf['Date'] = pd.to_datetime(df['Date'])  # Сначала конвертируй
df['Month'] = df['Date'].dt.month        # Потом извлекай

❌ Неправильно:
pythondf[df['Age'] > 40 & df['Gender'] == 'Female']  # Ошибка синтаксиса
✅ Правильно:
pythondf[(df['Age'] > 40) & (df['Gender'] == 'Female')]  # Скобки обязательны!

📖 Дополнительные ресурсы

Официальная документация: https://pandas.pydata.org/docs/
Pandas cheat sheet (PDF): https://pandas.pydata.org/Pandas_Cheat_Sheet.pdf
10 minutes to pandas: https://pandas.pydata.org/docs/user_guide/10min.html


Сохрани этот файл и держи открытым при работе с данными!