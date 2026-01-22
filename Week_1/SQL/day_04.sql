-- Day 4: SQLBolt Lessons 1–8 (Basics + Joins)

-- Basics (ORDER/LIMIT/OFFSET)
SELECT DISTINCT director
FROM movies
ORDER BY director;

SELECT title, year
FROM movies
ORDER BY year DESC
LIMIT 4;

SELECT title
FROM movies
ORDER BY title
LIMIT 5;

SELECT title
FROM movies
ORDER BY title
LIMIT 5 OFFSET 5;

-- North American cities (review style)
SELECT city, population
FROM north_american_cities
WHERE country = 'Canada';

SELECT city, latitude
FROM north_american_cities
WHERE country = 'United States'
ORDER BY latitude DESC;

SELECT city, longitude
FROM north_american_cities
WHERE longitude < -87.629798
ORDER BY longitude ASC;

SELECT city, population
FROM north_american_cities
WHERE country = 'Mexico'
ORDER BY population DESC
LIMIT 2;

SELECT city, population
FROM north_american_cities
WHERE country = 'United States'
ORDER BY population DESC
LIMIT 2 OFFSET 2;

-- JOIN: movies + boxoffice
SELECT movies.title, boxoffice.domestic_sales, boxoffice.international_sales
FROM movies
JOIN boxoffice ON movies.id = boxoffice.movie_id;

SELECT movies.title, boxoffice.domestic_sales, boxoffice.international_sales
FROM movies
JOIN boxoffice ON movies.id = boxoffice.movie_id
WHERE boxoffice.international_sales > boxoffice.domestic_sales;

SELECT movies.title, boxoffice.rating
FROM movies
JOIN boxoffice ON movies.id = boxoffice.movie_id
ORDER BY boxoffice.rating DESC;

-- LEFT JOIN + NULL checks (employees/buildings)
SELECT DISTINCT building
FROM employees
WHERE building IS NOT NULL;

SELECT building_name, capacity
FROM buildings;

SELECT DISTINCT b.building_name, e.role
FROM buildings b
LEFT JOIN employees e
  ON b.building_name = e.building;

SELECT name, role
FROM employees
WHERE building IS NULL;

SELECT b.building_name
FROM buildings b
LEFT JOIN employees e
  ON b.building_name = e.building
WHERE e.building IS NULL;