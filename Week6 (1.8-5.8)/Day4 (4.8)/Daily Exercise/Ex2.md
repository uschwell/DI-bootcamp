-- -- -- -- -- part 2.1
-- SELECT first_name, last_name, salary
-- FROM employees
-- WHERE salary BETWEEN 10000 AND 15000;





-- -- -- -- -- part 2.2
-- SELECT first_name, last_name, hire_date
-- FROM employees
-- WHERE year(hire_date)='1987';


-- -- -- -- -- part 2.3
-- SELECT *
-- FROM employees
-- WHERE first_name LIKE '%' + 'c' + '%' AND first_name LIKE '%' + 'e'+ '%';





-- -- -- -- -- part 2.4
-- SELECT last_name, job, salary
-- FROM employees
-- WHERE NOT job_id =9 AND NOT job_id =17 AND NOT salary=4500 AND NOT salary=10000 AND NOT salary=15000;




-- -- -- -- -- part 2.5
-- SELECT last_name
-- FROM employees
-- WHERE LEN(last_name)=6;





-- -- -- -- -- part 2.6
-- SELECT last_name
-- FROM employees
-- WHERE last_name LIKE '__e%';



-- -- -- -- -- part 2.7
-- SELECT DISTINCT(employees.job_id) AS temp, jobs.job_title
-- FROM employees, jobs
-- WHERE temp.job_id =jobs.job_id;



-- -- -- -- -- part 2.8
-- SELECT *
-- FROM employees
-- WHERE last_name LIKE 'BLAKE' OR last_name LIKE 'JONES' OR 
-- last_name LIKE 'SCOTT' OR last_name LIKE 'KING' OR last_name LIKE 'FORD';






