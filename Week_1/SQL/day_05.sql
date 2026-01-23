№ SQLBOLT Lesson 10-12

SELECT MAX(years_employed)
FROM employees;

SELECT role, AVG(years_employed)
FROM employees
GROUP BY role;

SELECT building, sum(years_employed)
FROM employees
GROUP BY building;

SELECT count(*) 
FROM employees 
WHERE role = "Artist";

SELECT role, count(*) 
FROM employees
GROUP BY role;

SELECT role, SUM(years_employed)
FROM employees
WHERE role = 'Engineer'
GROUP BY role;

SELECT director, COUNT(*)
FROM movies
GROUP BY director;

SELECT director, SUM(domestic_sales) + SUM(international_sales) AS total_sales
FROM boxoffice
INNER JOIN movies
    ON boxoffice.movie_id  = movies.id
GROUP BY director;

SELECT director, SUM(domestic_sales + international_sales) AS total_sales
FROM boxoffice
INNER JOIN movies
    ON boxoffice.movie_id = movies.id
GROUP BY director
HAVING total_sales > 1000000000
ORDER BY total_sales DESC;