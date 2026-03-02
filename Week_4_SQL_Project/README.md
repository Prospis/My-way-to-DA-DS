# ⚽ English Football Analysis - SQL Project

## 📊 Project Overview
SQL analysis of English football covering Premier League and Championship matches.

**Dataset:** 23,504 matches  
**Period:** 1993-2025  
**Tools:** SQLite, Window Functions, CTEs, JOINs

---

## 🎯 Business Questions Analyzed

### 1. Top Teams by Home Wins
**Question:** Which teams dominate at home?

**Key Finding:** Man United leads with 418 home wins

### 2. Goal Accumulation Analysis  
**Question:** How did Liverpool accumulate goals over seasons?

**Method:** Running total using `SUM() OVER(PARTITION BY Season)`

### 3. Home vs Away Performance
**Question:** Does home advantage exist?

**Key Finding:** 
- Home teams win **45.7%** of matches (5,563 wins)
- Away teams win **28.6%** (3,482 wins)
- **60% more wins at home!**

### 4. League Transitions
**Question:** Which teams moved between leagues?

**Key Finding:** 30+ teams played in both leagues. Leicester (18 PL / 10 Championship) is a classic yo-yo club.

---

## 🛠️ SQL Techniques Used

- ✅ Window Functions (RANK, SUM OVER, PARTITION BY)
- ✅ CTEs (WITH ... AS)
- ✅ INNER JOIN
- ✅ UNION ALL
- ✅ CASE statements
- ✅ COUNT DISTINCT

---

## 📁 Project Files

- `football.db` - SQLite database (23k+ matches)
- `analysis.sql` - All 4 SQL queries
- `README.md` - This file

---

## 💡 Key Insights

1. **Home advantage is real** - 60% more wins at home
2. **Man United = home fortress** - 418 wins (most in history)
3. **30+ yo-yo clubs** - High competition between leagues

---

## 📈 Next Steps

- Add time-series analysis (seasonal trends)
- Predict match outcomes
- Visualize with Power BI