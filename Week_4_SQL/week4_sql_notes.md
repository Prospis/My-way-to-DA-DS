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


SELECT  sale_date,
		region
        product,
  		revenue,
        MAX(revenue) OVER(PARTITION BY region) as max_in_region,
        revenue - MAX(revenue) OVER(PARTITION BY region) as diff_from_max
FROM sales
ORDER BY region;


WITH top_saller AS (
    SELECT 
        region, 
        salesperson, 
        SUM(revenue) as total_revenue, 
        RANK() OVER(PARTITION BY region ORDER BY SUM(revenue) DESC) as rank
    FROM sales
    GROUP BY region, salesperson
)
SELECT * FROM top_saller
WHERE rank = 1;


WITH
    seller_totals AS (
        SELECT
            salesperson,
            SUM(revenue) as total_revenue
        FROM sales
        GROUP BY salesperson
    ),
    top3_sellers AS (
        SELECT
            salesperson,
            total_revenue,
            RANK() OVER(ORDER BY total_revenue DESC) as rank
        FROM seller_totals
    )
SELECT 
	sales.*,
    total_revenue,
	top3_sellers.rank
FROM sales
JOIN top3_sellers ON sales.salesperson = top3_sellers.salesperson
WHERE top3_sellers.rank <= 3
ORDER BY top3_sellers.rank, sales.sale_date;


WITH
    avg_region AS (
        SELECT
            region,
      		AVG(revenue) as avg_revenue
        FROM sales
        GROUP BY region
    )
SELECT 
	sales.*,
   	ROUND(avg_region.avg_revenue, 2)
	
FROM sales
JOIN avg_region ON sales.region = avg_region.region
WHERE sales.revenue > avg_region.avg_revenue
ORDER BY sales.region;


WITH ConsecutiveNums AS (  
		SELECT
			num,
			(num = Lead(num,1)  OVER (ORDER by id)
    		AND
    		num = Lead(num,2)  OVER (ORDER by id)) as nums 
		FROM Logs
)
SELECT DISTINCT num AS ConsecutiveNums
FROM ConsecutiveNums
WHERE nums = 1;


WITH 
	max_salary AS (
      	SELECT
      		name,
      		salary,
      		departmentId,
      		RANK() OVER(PARTITION BY departmentId ORDER by salary desc) as rank
		FROM Employee
)

SELECT
		Department.name as Department,
        max_salary.name as Employee,
        max_salary.salary AS Salary
FROM max_salary
JOIN Department ON max_salary.departmentId = Department.id
WHERE rank = 1;      
    


    WITH sal as (
	SELECT
    	salary,
    	DENSE_RANK() OVER(ORDER BY salary DESC) AS rank
	FROM Employee
)
SELECT(
   SELECT DISTINCT salary 
FROM sal
WHERE rank = 4)
AS getNthHighestSalary;





SELECT 
	id,
    CASE
    	WHEN id % 2 = 1 THEN COALESCE(LEAD(student,1) OVER(ORDER BY id),student)
        ELSE LAG(student,1) OVER(ORDER BY id)
    END as swapped_student
    
FROM Seat;





SELECT
	email as Email
FROM Person
GROUP by email
HAVING COUNT(id) > 1



SELECT
	score,
    DENsE_RANK() OVER(ORDER BY score DESC) as rank
FROM Scores




WITH temperatura AS(
  SELECT
	id,
    temperature > LAG(temperature) OVER(ORDER BY recordDate) as rec
  FROM Weather
  )
SELECT id
FROM temperatura
Where rec = 1;