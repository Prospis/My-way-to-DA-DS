# 🤖 КОНТЕКСТ ДЛЯ CLAUDE: Rustam's Data Analyst Journey

**Дата последнего обновления:** 17.02.2026 (Вторник, начало недели 4)

---

## 👤 О студенте

**Имя:** Рустам (Rustam)  
**Цель:** Стать Junior Data Analyst и устроиться на работу в США  
**Срок:** 20-22 недели (~5 месяцев, до июня 2026)  
**Локация:** Palatine, Illinois, US

### **Особенности обучения:**
1. ⚠️ **Забывает синтаксис** на следующий день → нужно повторение и шпаргалки
2. ⚠️ **Нужна теория перед практикой** → объяснения с аналогиями обязательны
3. ✅ **Честный и открытый** → говорит, когда не понимает или устал
4. ✅ **Пишет код сам** → не копирует готовые решения
5. ✅ **Хочет думать самостоятельно** → просит задания БЕЗ готового кода
6. ⚠️ **Работает параллельно** → учится 4-6 часов в день (пн-пт), нужны гибкие сессии

### **ВАЖНО: Методология обучения Рустама**
**Рустам учится лучше всего когда:**
- ❌ НЕТ готового кода в ответах Claude
- ✅ ЕСТЬ только задания и логика
- ✅ Подсказки даются ТОЛЬКО если застрял
- ✅ Проверка результата после выполнения

**Баланс:**
- Слишком мало помощи → фрустрация
- Готовый код → не запоминает
- **Идеально:** Задание + подсказки по запросу

### **Проблема, которую решили:**
- **Было:** Работал с 4 AI (Claude, Grok, Gemini, GPT) → потеря контекста, путаница
- **Стало:** Работает ТОЛЬКО с Claude → чёткий прогресс, единая методология

---

## 📚 Пройденный материал

### ✅ **Неделя 1 (19-23 января 2026):**
- Python basics (syntax, loops, functions, data structures)
- SQL basics (SQLBolt уроки 1-8, 10-12: SELECT, WHERE, JOIN, GROUP BY, ORDER BY)

**Результат:** Понимает основы Python и SQL

---

### ✅ **Неделя 2 (26 января-6 февраля 2026):**

**Контекст перезапуска:**
- 29-30.01: Рустам застрял на визуализации, почувствовал "ничего не понимаю"
- 31.01-04.02: AI Council эксперимент (multi-agent система) → добавил сложности вместо ясности
- 05-06.02: Решил упростить → работа только с Claude

**День 1-4 (06.02): Pandas + Visualization**
- Exploration: `.info()`, `.describe()`, `.head()`
- Cleaning: datetime conversion, новые колонки, проверка данных
- Analysis: метрики, группировки, фильтрация
- Visualization: 6 типов графиков (bar, pie, line, histogram, heatmap, box)

**День 5 (09.02): Mini-Project**
- Executive Summary (4 ключевых инсайта)
- Business Recommendations (4 стратегии)
- README.md для портфолио
- GitHub push

**Результат недели 2:**
- ✅ Освоил pandas (exploration, cleaning, analysis)
- ✅ Создал профессиональные графики
- ✅ Нашёл бизнес-инсайты
- ✅ Портфолио-проект готов

**Файл:** `Week_2_Restart/week_03_day_01-05.ipynb`

---

### ✅ **Неделя 3 (9-16 февраля 2026): Advanced Pandas + Seaborn + Kaggle Project**

**День 1 (9.02): Advanced Pandas**

**Изучено:**
1. **`.merge()` — объединение таблиц**
   - INNER JOIN vs LEFT JOIN
   - Практика с customers + orders
   
2. **`.pivot_table()` — сводные таблицы**
   - Многомерный анализ (город × продукт)
   - Разные функции агрегации

3. **`lambda` и `.apply()`**
   - Категоризация клиентов по тратам
   - Вложенные условия

4. **`.groupby()` с `.agg()`**
   - Множественная агрегация
   - Именованные агрегации

**Домашнее задание выполнено:**
- ✅ Средний возраст по городам
- ✅ Pivot table с количеством заказов
- ✅ Клиент с поздним первым заказом

**Файл:** `Week_3/advanced_pandas_day_01-05.ipynb`

---

**День 2 (10.02): Выходной** (работа)

**День 3 (11.02): GitHub + Context Update** (30 минут)

---

**День 4 (12.02): Seaborn Deep Dive**

**Освоено:**
1. **`sns.pairplot()`** — матрица графиков для EDA
   - Все взаимосвязи между переменными сразу
   - Распределения на диагонали
   - Scatter plots вне диагонали

2. **`sns.violinplot()`** — пропущен (мало данных, вернёмся на Kaggle)

3. **`sns.jointplot()`** — scatter + 2 histograms
   - Анализ связи age vs amount
   - Weak positive correlation
   - Линия тренда + доверительный интервал

4. **`sns.catplot()`** — категориальные данные
   - Средняя цена по продуктам
   - Laptop $1200, Mouse $50

**Ключевые концепции освоены:**
- Scientific notation (e+12) = Unix timestamps
- Percentiles (25%, 50%, 75%) = квартили
- Когда использовать каждый тип графика

**Kaggle Project Started:**
- Датасет: Uber & Lyft Cab Prices (693k rides, 6k weather)
- Exploration completed
- Cleaning started:
  - Converted time_stamp to datetime
  - Created time features (year, month, day, hour)
  - Filled missing prices (median by product_name)
  - Filled missing rain values

**Файлы:**
- `Week_3/images/` — 5 Seaborn visualizations
- `Week_3_Project/uber_lyft_analysis.ipynb` — начат проект

---

**День 5 (13.02): Uber/Lyft Merge & Analysis**

**Completed:**
1. **Data Merge:**
   - Rounded time to hour (`.dt.floor('h')`)
   - Removed weather duplicates (6276 → 3960 unique)
   - Merged rides + weather: 693k rows
   - 99.6% rides matched with weather (690k/693k)

2. **Initial Analysis:**
   - Uber average: $15.47
   - Lyft average: $17.35 (12% more expensive!)
   - Average temperature: 39.2°F (4°C)
   - Price by vehicle type analyzed

**Понял важные концепции:**
- Зачем округлять время до часа (погода меняется медленно)
- Как merge работает с временными данными
- Почему возникают дубликаты при merge
- Как их избежать (`drop_duplicates` перед merge)

**Файл:** `Week_3_Project/uber_lyft_analysis.ipynb`

---

**День 6 (16.02): Завершение Uber/Lyft Project**

**Completed:**
1. **Бизнес-анализ:**
   - Проверена корреляция rain vs price (0.0008 = нет влияния)
   - Проверена динамика цен по часам (минимальная разница)
   - Топ типов машин (все одинаковые ~55k поездок = искусственный датасет)

2. **5 Визуализаций:**
   - Bar Chart: Uber vs Lyft средние цены
   - Bar Chart: Топ-13 типов машин по цене
   - Histogram: Распределение цен (отфильтровано до $50, показано 99.7% данных)
   - Line Chart: Цены по месяцам (только ноябрь-декабрь 2018)
   - Box Plot: Разброс цен Uber vs Lyft

3. **README.md:**
   - Key Findings (4 инсайта)
   - Tools Used
   - Files structure
   - **Limitations section** (датасет 2 месяца, искусственно сбалансирован)

4. **GitHub Push:**
   - Все файлы в Week_3_Project/
   - Главный README обновлён
   - Week 3 отмечена как завершённая

**Ключевые уроки Week 3:**
- ✅ Реальные Kaggle датасеты могут быть ограниченными
- ✅ Не каждый датасет даёт интересные инсайты (это нормально!)
- ✅ Критическое мышление: понимание ограничений данных
- ✅ Работа с большими датасетами (693k строк)
- ✅ Time-based merging (округление до часа)
- ✅ Фильтрация выбросов для читаемости графиков

**Результат недели 3:**
- ✅ Advanced Pandas освоен (merge, pivot_table, lambda, apply, agg)
- ✅ Seaborn практика (4 типа графиков)
- ✅ Первый реальный Kaggle проект завершён
- ✅ Профессиональный README с критической оценкой

**Файлы:**
- `Week_3/advanced_pandas_day_01-05.ipynb`
- `Week_3/images/` (5 Seaborn графиков)
- `Week_3_Project/uber_lyft_analysis.ipynb`
- `Week_3_Project/images/` (5 финальных визуализаций)
- `Week_3_Project/README.md`

---

## 📅 ТЕКУЩИЙ ПЛАН

### **Неделя 4 (17-21.02): SQL Advanced** ← ТЕКУЩАЯ НЕДЕЛЯ

#### **Цель недели:**
Освоить продвинутый SQL для технических интервью и сложных проектов

#### **Почему SQL Advanced сейчас:**
1. Спрашивают на 90% интервью для Junior DA
2. Прошло 3 недели с Week 1 — нужно освежить + углубить
3. Быстро освоить: 1 неделя теории + практики + проект
4. Откроет возможность делать более сложный анализ

---

#### **✅ Вторник (17.02): Планирование + SQL Basics Refresh**
**План:**
1. Обновить `claude_context.md` (30 мин) ✅
2. Спланировать Week 4 (30 мин) ✅
3. Повторить SQL basics (30-60 мин):
   - SELECT, WHERE, JOIN
   - GROUP BY, HAVING, ORDER BY
   - Практика на SQLBolt (уроки 1-8 быстрый прогон)

**DoD:** Вспомнил базовый SQL, готов к Window Functions

---

#### **⏳ Среда-Четверг (18-19.02): Window Functions + CTEs**

**Среда (18.02): Window Functions**
- Теория: что такое Window Functions, зачем нужны
- Основные функции:
  - `ROW_NUMBER()` — нумерация строк
  - `RANK()` / `DENSE_RANK()` — ранжирование
  - `LAG()` / `LEAD()` — доступ к предыдущим/следующим строкам
  - `SUM() OVER()` / `AVG() OVER()` — running totals
- Практика на примерах
- LeetCode SQL (2-3 задачи)

**Четверг (19.02): CTEs + Практика**
- Теория: Common Table Expressions (CTEs)
- Зачем нужны: читаемость, рекурсия
- CTE vs Subquery
- Практика на LeetCode SQL (3-4 задачи Window Functions + CTEs)

**DoD:** Понимаю Window Functions и CTEs, могу решать задачи

---

#### **⏳ Пятница-Суббота (20-21.02): SQL Mini-Project**

**Опция A: Standalone SQL Project**
- Найти датасет с временными данными (sales, events)
- Применить Window Functions для анализа
- Создать SQL скрипты с комментариями
- README + GitHub push

**Опция B: Добавить SQL к существующему проекту**
- Взять датасет из Week 2 или Week 3
- Импортировать в SQLite
- Написать SQL запросы с Window Functions
- Сравнить Pandas vs SQL подход

**DoD:** SQL проект в портфолио, готов отвечать на SQL вопросы на интервью

---

### **Неделя 5 (23-27.02): TBD**
Опции:
- Новый интересный Kaggle проект
- Power BI / Tableau basics
- Statistics basics

Решим в конце Week 4.

---

## 🎯 РОЛИ CLAUDE

### **🏗️ Architect (Планирование)**
**Когда:** Начало недели, выбор инструментов  
**Триггер:** "Claude-Architect, помоги спланировать..."

### **🔍 Critic (Проверка)**
**Когда:** Ревью кода, проверка ноутбуков  
**Триггер:** "Claude-Critic, проверь мой код..."

### **🛠️ Tech (Техническая помощь)**
**Когда:** Застрял в коде, не понимаю концепцию  
**Триггер:** "Claude-Tech, объясни/помоги..."  
**ВАЖНО:** НЕ давать готовый код! Только задания + подсказки.

### **🎓 Mentor (Мотивация и поддержка)**
**Когда:** Потеря мотивации, прокрастинация  
**Триггер:** "Claude-Mentor, мне нужна поддержка..."

---

## 📝 МЕТОДОЛОГИЯ ОБУЧЕНИЯ

### **Принципы:**
1. **Теория → Практика → Рефлексия**
2. **НЕ давать готовый код** — только задания БЕЗ кода
3. **Качество > Скорость**
4. **Шпаргалки обязательны**

### **Правильный формат ответов Tech:**

**❌ НЕПРАВИЛЬНО:**
```python
# Готовое решение
df.groupby('city')['price'].mean()
```

**✅ ПРАВИЛЬНО:**
```
Задание: Посчитай среднюю цену по городам

Шаги:
1. Сгруппируй датасет по городу
2. Выбери колонку с ценой
3. Посчитай среднее

Подсказки (если застрянешь):
- Для группировки используй .groupby()
- Для среднего используй .mean()
```

---

## ⚠️ КРАСНЫЕ ФЛАГИ

1. **"Ничего не понимаю"** → Остановиться, объяснить по-другому
2. **"Я устал"** → Закончить день
3. **Забывает вчерашний материал** → Повторение
4. **"У меня работа"** → Гибкий график
5. **"Дай готовый код"** → Напомнить о методологии (учится лучше сам!)

---

## 🗂️ ФАЙЛЫ И СТРУКТУРА

```
My-way-to-DA-DS/
├── Week_1/ (Python + SQL basics)
├── Week_2/ (Старая попытка)
├── Week_2_Restart/ (Pandas + Visualization — завершён)
├── Week_3/ (Advanced Pandas + Seaborn)
│   ├── advanced_pandas_day_01-05.ipynb
│   └── images/ (5 Seaborn графиков)
├── Week_3_Project/ (Uber/Lyft Analysis — ЗАВЕРШЁН ✅)
│   ├── data/ (cab_rides.csv, weather.csv — НЕ в git)
│   ├── images/ (5 финальных визуализаций)
│   ├── uber_lyft_analysis.ipynb
│   └── README.md
├── claude_context.md (ЭТОТ ФАЙЛ)
├── claude_roles.md
├── council_log.md
└── README.md (обновлён: Week 3 завершена)
```

---

## 🎯 СЛЕДУЮЩАЯ СЕССИЯ (Вторник, 17.02.2026 — СЕГОДНЯ)

### **Текущий статус:**
- Обновление контекста ✅
- Планирование Week 4 ✅
- Осталось: SQL Basics Refresh

### **План на оставшееся время сегодня:**
1. Быстрое повторение SQL basics (30-60 мин)
   - SQLBolt уроки 1-8 (быстрый прогон)
   - Вспомнить: SELECT, JOIN, GROUP BY, ORDER BY
2. Подготовиться к завтрашнему дню (Window Functions)

**DoD сегодня:** Вспомнил базовый SQL, готов к Window Functions завтра

---

## 💡 ВАЖНЫЕ ЗАМЕТКИ

### **О темпе Week 3:**
- Неделя 3 заняла 6 дней (9-16 февраля, с выходными/работой)
- Это НОРМАЛЬНО и КАЧЕСТВЕННО
- Uber/Lyft проект = первый реальный Kaggle датасет (693k строк)
- Лучше 1 качественный проект, чем 3 поверхностных

### **О стиле обучения:**
- Рустам СИЛЬНО просит НЕ давать готовый код
- Это его способ глубокого обучения
- Claude должен давать ЗАДАНИЯ, не РЕШЕНИЯ
- Подсказки — только по запросу

### **Об Uber/Lyft проекте:**
- Первый реальный Kaggle датасет
- 693k строк — серьёзный объём
- Практика merge с временными данными
- Важный урок: не все датасеты интересные (критическое мышление)
- Отличный кейс для портфолио (показывает умение работать с ограничениями)

### **О SQL:**
- Week 1 был 3 недели назад — нужно освежить
- SQL средний уровень (SELECT/JOIN/GROUP BY понимает)
- Window Functions — ключевой скилл для интервью
- Быстро освоить: 1 неделя достаточно

---

## 📞 КАК МЕНЯ ИСПОЛЬЗОВАТЬ

**В начале КАЖДОЙ сессии:**
1. Загрузи `claude_context.md`
2. Скажи какая роль нужна
3. Если Tech — помни: ЗАДАНИЯ БЕЗ КОДА!

**Пример:**
```
Привет Claude! Вот claude_context.md

Claude-Tech, готов повторить SQL basics!
С чего начнём?
```

---

## ✅ ОБНОВЛЕНИЯ ЭТОГО ФАЙЛА

**Последнее обновление:** 17.02.2026 (вторник, начало недели 4)

**Что изменилось:**
- Добавлен полный отчёт Week 3 (дни 1-6)
- Uber/Lyft проект завершён и задокументирован
- Добавлен детальный план Week 4 (SQL Advanced)
- Обновлена следующая сессия (сегодня: SQL basics refresh)
- Обновлена структура файлов

**Следующее обновление:** Конец недели 4 (21.02.2026)

---

**Конец файла контекста. Версия: 4.0 от 17.02.2026**


## Неделя 4: SQL Advanced (17-21 февраля, 2-3 марта 2026)

### День 1-2 (17-18 февраля): SQL Basics Refresh + Window Functions
**Что освоил:**
- SQL Basics: SELECT, WHERE, GROUP BY, JOIN
- Window Functions: ROW_NUMBER, RANK, DENSE_RANK
- LAG/LEAD для сравнения с предыдущими/следующими строками
- SUM OVER для накопительных сумм
- PARTITION BY для группировки внутри Window Functions

**База данных:** 
- Создал `sales` таблицу (20 строк, 4 региона, 4 продавца)
- Работал на sqliteonline.com

**Практика:**
- 4 задачи на SQL Basics
- 6 задач на Window Functions
- Всё решал самостоятельно

### День 3 (19 февраля): CTEs + LeetCode SQL

**Что освоил:**
- CTEs (Common Table Expressions): WITH ... AS
- Множественные CTEs (разделение запятыми)
- CASE statements для условной логики
- COALESCE для обработки NULL

**LeetCode Medium задачи (7 из 7):**
1. ✅ Consecutive Numbers (LAG/LEAD)
2. ✅ Department Highest Salary (RANK + CTE + JOIN)
3. ✅ Nth Highest Salary (DENSE_RANK)
4. ✅ Exchange Seats (CASE + COALESCE + LEAD/LAG)
5. ✅ Rank Scores (DENSE_RANK)
6. ✅ Duplicate Emails (GROUP BY + HAVING)
7. ✅ Rising Temperature (LAG + CTE)

**Что было сложно:**
- VS Code настройка для SQL (потратили 2 часа!)
- Решение: использовал sqliteonline.com

### ПАУЗА: 24 февраля - 2 марта (неделя восстановления)

**Причина:** Выгорание после 5 недель интенсивной учёбы
- Работа + учёба = двойная нагрузка
- Давление от жены (основной кормилец)
- Усталость, приболел

**Решение:** Полная неделя отдыха без учёбы

**Результат:** 
- ✅ Восстановил энергию
- ✅ Вернулся с мотивацией
- ✅ Готов продолжать

### День 4-5 (3 марта): SQL Mini-Project завершён!

**Dataset:** English Football (Premier League + Championship)
- 23,504 матчей (1993-2025)
- 2 таблицы: premier_league (12,153), championship (11,351)

**SQL Запросы (4 завершённых):**
1. ✅ Топ-10 команд по домашним победам (RANK, CTE, GROUP BY)
2. ✅ Running total голов Liverpool (SUM OVER, PARTITION BY, UNION ALL)
3. ✅ Home vs Away статистика (CASE, UNION ALL)
4. ✅ Переходы между лигами (INNER JOIN, COUNT DISTINCT)

**Ключевые инсайты:**
- 🏆 Man United — 418 домашних побед (лидер всех времён)
- 🏠 Домашнее преимущество: 45.7% побед дома vs 28.6% в гостях (+60%!)
- 🔄 30+ команд играли в обеих лигах (высокая конкуренция)
- 🎢 Leicester — классический yo-yo клуб (18 PL / 10 Championship сезонов)

**Технические навыки:**
- Window Functions (RANK, SUM OVER, PARTITION BY)
- CTEs (WITH ... AS)
- JOINs (INNER JOIN)
- CASE statements
- UNION ALL
- COUNT DISTINCT

**Документация:**
- ✅ Профессиональный README.md
- ✅ Git push выполнен

**Время:** 2 часа (вместо запланированных 4-5)

**Что понял:**
- Отдых был необходим — вернулся продуктивнее
- Упрощение задачи (4 вместо 7 запросов) — правильное решение
- Не сдаваться после выгорания — ключевой навык

---

## 📊 Статус Week 4:
- [x] SQL Basics Refresh
- [x] Window Functions
- [x] CTEs
- [x] LeetCode (7 задач Medium)
- [x] SQL Mini-Project ✅

---

## 🎓 Навыки после Week 4:
**SQL:** Прохожу 70-80% SQL интервью для Junior DA
- SELECT, WHERE, GROUP BY, JOIN ✅
- Window Functions (RANK, LAG, LEAD, SUM OVER) ✅
- CTEs ✅
- CASE, COALESCE ✅
- Агрегатные функции ✅

**Портфолио:** 3 проекта
1. Retail Sales Analysis (Pandas)
2. Uber/Lyft Analysis (Advanced Pandas + Merge)
3. English Football Analysis (SQL) ← НОВЫЙ!


## Неделя 5: SQL LeetCode Practice (5-6 марта 2026)

### **День 1 (5 марта, четверг): LeetCode Easy (2 часа)**

**Что сделал:**
- Решил 12 задач Easy уровня
- Освоил новые SQL паттерны

**Задачи Easy (12/12):**
1. ✅ 175 - Combine Two Tables (LEFT JOIN)
2. ✅ 181 - Employees Earning More (Self-Join)
3. ✅ 182 - Duplicate Emails (GROUP BY + HAVING)
4. ✅ 183 - Customers Who Never Order (LEFT JOIN + IS NULL)
5. ✅ 196 - Delete Duplicate Emails (DELETE + Self-Join)
6. ✅ 197 - Rising Temperature (LAG + DATEDIFF)
7. ✅ 511 - Game Play Analysis I (MIN + GROUP BY)
8. ✅ 577 - Employee Bonus (LEFT JOIN + NULL handling)
9. ✅ 584 - Find Customer Referee (IS NULL vs != )
10. ✅ 586 - Customer Placing Largest Orders (COUNT + ORDER BY)
11. ✅ 595 - Big Countries (OR conditions)
12. ✅ 596 - Classes More Than 5 Students (HAVING)

**Новые навыки:**
- Self-Join (таблица соединяется сама с собой)
- IS NULL / IS NOT NULL (правильная работа с NULL)
- DELETE с JOIN
- DATEDIFF, DATE_ADD, DATE_SUB
- Backticks для зарезервированных слов

**Что было сложно:**
- Self-Join — новая концепция, но разобрался
- NULL handling — запомнил IS NULL вместо = NULL
- Зарезервированные слова (rank) — научился использовать backticks

---

### **День 2 (6 марта, пятница): LeetCode Medium (5 часов)**

**Что сделал:**
- Решил 6 задач Medium уровня
- Создал первую SQL функцию!

**Задачи Medium (6/6):**
1. ✅ 176 - Second Highest Salary (DENSE_RANK + Subquery для NULL)
2. ✅ 177 - Nth Highest Salary (CREATE FUNCTION!)
3. ✅ 178 - Rank Scores (DENSE_RANK + Backticks)
4. ✅ 180 - Consecutive Numbers (LAG + LEAD логика)
5. ✅ 184 - Department Highest Salary (PARTITION BY + JOIN)
6. ✅ 550 - Game Play Analysis IV (DATE_ADD + Complex JOIN + Fraction)

**Новые навыки:**
- **SQL Functions** (CREATE FUNCTION, RETURN) — впервые!
- PARTITION BY для группировки внутри Window Functions
- Сложные JOIN с датами (DATE_ADD)
- Subquery для возврата NULL
- Fraction calculations (деление COUNT)

**Ключевые концепции:**
- RANK vs DENSE_RANK:
  - RANK пропускает номера после дубликатов (1,2,2,4)
  - DENSE_RANK не пропускает (1,2,2,3)
  - Для "N-я по величине" используй DENSE_RANK!

- LAG/LEAD для "подряд идущих":
  - LAG(col, 1) = предыдущая строка
  - LEAD(col, 1) = следующая строка
  - LAG(col, 2) = через одну назад (не нужно для "3 подряд"!)

- PARTITION BY vs GROUP BY:
  - GROUP BY сворачивает строки
  - PARTITION BY сохраняет все строки, но делит на группы для Window Function

**Что было сложно:**
- SQL Functions — новая тема, освоил за 5 минут!
- LEAD(num, 2) vs LEAD(num, 1) — разобрался в логике
- Забыл FROM в SELECT — нашёл ошибку сам!
- Runtime оптимизация — решение работает, но медленное (это OK!)

**Что понял о себе:**
- Нахожу ошибки сам (забыл FROM — исправил до ответа Claude)
- Задаю правильные вопросы ("почему LEAD 2?", "что если 4 подряд?")
- Учусь на ошибках (backticks после первой ошибки с rank)

---

## 📊 Итоги Week 5:

**Всего задач решено:** 18 за 2 дня! 🔥
- Easy: 12/12 ✅
- Medium: 6/6 ✅

**Время:** 7 часов (2ч + 5ч)  
**Темп:** 2.6 задачи в час — отличная скорость!

**SQL навыки после Week 5:**
- Базовый SQL: SELECT, WHERE, JOIN, GROUP BY ✅
- Window Functions: RANK, DENSE_RANK, LAG, LEAD, PARTITION BY ✅
- CTEs (WITH ... AS) ✅
- Self-Join ✅
- NULL handling (IS NULL) ✅
- Date functions (DATEDIFF, DATE_ADD) ✅
- DELETE operations ✅
- **SQL Functions (CREATE FUNCTION)** ✅ — новое!
- Сложные комбинации (CTE + Window + JOIN) ✅

**Готовность к SQL интервью:** 70-80% для Junior DA! 🎯

---

## 🎓 Портфолио после Week 5:

1. ✅ Retail Sales Analysis (Pandas, Week 2)
2. ✅ Uber/Lyft Analysis (Advanced Pandas, Week 3)
3. ✅ English Football Analysis (SQL Advanced, Week 4)
4. ✅ **18 LeetCode задач** (SQL Practice, Week 5) ← НОВОЕ!

**GitHub:** My-way-to-DA-DS  
**LeetCode Profile:** 18 SQL задач решено

---

## 💪 Общий прогресс (5 недель):

**Python/Pandas:** Junior-ready (80%) ✅  
**SQL:** Junior-ready (80%) ✅  
**Visualization:** Базовый уровень (40%)  
**Statistics:** Не начинал (0%)  
**BI Tools:** Не начинал (0%)  

**Оценка готовности к Junior DA роли:** 60-65%

**Можно начинать рассылку резюме** с акцентом на SQL + Python позиции! 🚀

---

## 🎯 Что дальше:

**Варианты:**

**A) Week 6: Statistics Basics**
- Measures of Central Tendency
- Probability & Correlation
- Hypothesis Testing
- A/B Testing mini-project

**B) Week 6: Power BI / Tableau**
- Визуализация данных
- Дашборды
- Ещё один проект в портфолио

**C) Начать рассылку резюме прямо сейчас**
- Уже есть 3 проекта + 18 LeetCode
- Достаточно для Junior позиций
- Можно учиться параллельно с поиском работы

**Решение:** Обсудим в следующей сессии

---

## 🔥 Ключевое достижение Week 5:

**Преодолел прокрастинацию!**

Цитата от начала недели:
> "из-за того что я чувствую что не понимаю что-то, или мне кажется это сложным, у меня отпускаются руки и нет желания садиться за комп"

**Результат:**
- Не побоялся LeetCode
- Решил 18 задач за 2 дня
- Освоил новые концепции (Self-Join, SQL Functions)
- **Не сдался!** 💪

**Вывод:** Страх сложности был иллюзией. Когда начал делать — оказалось посильно!

---

**Последнее обновление:** 6 марта 2026 (пятница, конец недели 5)  
**Следующее обновление:** После Week 6 или после решения о поиске работы

---

**Конец Week 5. Версия council_log: 4.0**