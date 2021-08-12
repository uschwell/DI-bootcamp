-- -- -- -- -- part 1.1
-- SELECT first_name, last_name
-- FROM employees;



-- -- -- -- -- part 1.2
-- SELECT DISTINCT first_name, last_name
-- FROM employees;


-- -- -- -- -- part 1.3
-- SELECT *
-- FROM employees
-- ORDER BY first_name DESC;


-- -- -- -- -- part 1.4

-- -- -- -- -- couldnt understand what was wanted/needed here that wasn't in 1.3



-- -- -- -- -- part 1.5
-- SELECT employee_id, first_name, last_name, salary
-- FROM employees
-- ORDER BY salary ASC;




-- -- -- -- -- part 1.6
SELECT SUM(salary)
FROM employees;



-- -- -- -- -- part 1.7
-- SELECT employee_id, first_name, last_name, salary
-- FROM employees
-- ORDER BY salary ASC;




-- -- -- -- -- part 1.8
-- SELECT MAX(salary), MIN(salary)
-- FROM employees;




-- -- -- -- -- part 1.9
SELECT COUNT(*)
FROM employees;

-- -- -- --NOTE: Could also have just returned the 'highest' employee ID (since it is unique and incremented with each employee)





-- -- -- -- -- part 1.10
SELECT UPPER(first_name) AS MyUpperCase
FROM employees;


-- -- -- -- -- part 1.11
-- SELECT SUBSTRING(first_name, 1, 3)
-- FROM employees;


-- -- -- -- -- part 1.12
-- SELECT (first_name, last_name) AS full_name
-- FROM employees;


-- -- -- -- -- part 1.13
-- SELECT LEN((first_name, last_name) AS full_name), first_name, last_name
-- FROM employees;



-- -- -- -- -- part 1.14
-- SELECT first_name 
-- FROM  employees 
-- WHERE first_nameLIKE '%[0-9]%';




-- -- -- -- -- part 1.15
-- -- -- -- -- I used the generic "table", for use: replace with name of the relevant table you wish to query
-- SELECT *
-- FROM  "table"
-- LIMIT(10);




