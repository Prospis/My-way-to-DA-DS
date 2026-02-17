SELECT * FROM employees;

SELECT name, salary FROM employees
WHERE department = 'IT'

SELECT employees.name, projects.project_name
FROM employees
JOIN projects ON employees.id = projects.employee_id;


SELECT department, AVG(salary) AS avg_salary
FROM employees
GROUP BY department
HAVING avg_salary > 60000


SELECT name, salary
FROM employees
ORDER BY salary DESC
LIMIT 3;



SELECT 
    name, 
    department,
    salary,
    ROW_NUMBER() OVER(ORDER BY salary DESC) as row_num
FROM employees;


SELECT 
    name, 
    department,
    salary,
    ROW_NUMBER() OVER(PARTITION BY department ORDER BY salary DESC) as dept_rank
FROM employees
ORDER BY department, dept_rank;


SELECT * FROM (
    SELECT 
        name, 
        department,
        salary,
        RANK() OVER(PARTITION BY department ORDER BY salary) as dept_rank
    FROM employees
) 
WHERE dept_rank <= 2;

SELECT 
    sale_date,
    product,
    revenue,
    SUM(revenue) OVER(ORDER BY sale_date) AS running_total
FROM sales;

SELECT * FROM (
    SELECT 
        region,
        salesperson,
        SUM(revenue) AS total_revenue,
        RANK() OVER(PARTITION BY region ORDER BY SUM(revenue) DESC) as rank
    FROM sales
    GROUP BY region, salesperson
)
WHERE rank = 1;


SELECT 
    region,
    product,
    SUM(revenue) as total_revenue,
    RANK() OVER(PARTITION BY region ORDER BY SUM(revenue)) as product_rank
FROM sales
GROUP BY region, product
ORDER BY region, product_rank;



SELECT  sale_date,
        product,
  		revenue,
        LAG(revenue) OVER(ORDER BY sale_date) AS prev_revenue,
        revenue - LAG(revenue) OVER(ORDER BY sale_date) as change
FROM sales
WHERE salesperson = 'Alice'
ORDER BY sale_date;



SELECT  sale_date,
        product,
  		revenue,
        ROUND((revenue *1.0 / SUM(revenue) OVER()) * 100,2)  as pct_of_total
FROM sales
ORDER BY sale_date;


