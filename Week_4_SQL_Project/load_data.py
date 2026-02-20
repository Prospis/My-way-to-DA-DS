import pandas as pd
import sqlite3

# Создаём базу данных
conn = sqlite3.connect('football.db')

# Загружаем Premier League
print("Loading Premier League data...")
premier_league = pd.read_csv('data/EnglandPL.csv')  
premier_league.to_sql('premier_league', conn, if_exists='replace', index=False)
print(f"Premier League: {len(premier_league)} matches loaded")

# Загружаем вторую лигу
print("Loading Championship data...")
championship = pd.read_csv('data/England_Championship.csv')  # Замени на имя второго файла
championship.to_sql('championship', conn, if_exists='replace', index=False)
print(f"Championship: {len(championship)} matches loaded")

conn.close()
print("✅ Database created: football.db")