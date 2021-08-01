-- CREATE DATABASE bootcamp
--     WITH 
--     OWNER = postgres
--     ENCODING = 'UTF8'
--     LC_COLLATE = 'English_Israel.1252'
--     LC_CTYPE = 'English_Israel.1252'
--     TABLESPACE = pg_default
--     CONNECTION LIMIT = -1;


-- CREATE TABLE students(
-- _id SERIAL PRIMARY KEY,
-- first_name VARCHAR (50) NOT NULL,
-- last_name VARCHAR (50) NOT NULL,
-- birth_date DATE NOT NULL
-- )
-- ;

-- INSERT INTO students (first_name, last_name,birth_date)
-- VALUES('Marc','Benichou', '1998/11/02'),
-- ('Yoan','Cohen','2010/11/03'),
-- ('Lea','Benichou','1987/07/27'),
-- ('Amelia','Dux','1996/04/07'),
-- ('David','Grez','2003/06/14'),
-- ('Omer','Simpson','1980/10/03'),
-- ('Uri','Schwell','1992/10/13')
-- ;

-- -- -- Step 1
-- SELECT * FROM students;

-- -- -- Step 2
-- SELECT first_name, last_name FROM students;

-- -- -- Step 3
-- -- -- -- I deliberatly added the the _id number to be printed (step 3.1)
-- SELECT _id,first_name, last_name FROM students WHERE _id=2

-- -- -- -- Step 3.2
-- SELECT first_name, last_name FROM students WHERE last_name = 'Benichou' AND first_name = 'Marc'

-- -- -- -- Step 3.3 (I assumed both first AND last names being correct is also permitted (i.e not xor))
-- SELECT first_name, last_name FROM students WHERE last_name = 'Benichou' OR first_name = 'Marc'

-- -- -- -- Step 3.4
-- SELECT first_name, last_name FROM students WHERE first_name LIKE '%a%';

-- -- -- -- Step 3.5
-- SELECT first_name, last_name FROM students WHERE first_name LIKE 'a%';

-- -- -- -- Step 3.6
-- SELECT first_name, last_name FROM students WHERE first_name LIKE '%a';

-- -- -- -- Step 3.7
-- SELECT first_name, last_name FROM students WHERE first_name LIKE '%a';

-- -- -- -- Step 3.8 -Maybe I misunderstood this one-but NO-ONE can meet this. each ID is singular its either 1 OR 3 not BOTH
-- SELECT first_name, last_name FROM students WHERE _id=1 AND _id=3;


-- -- -- -- Step 4
-- -- DECLARE { @myDate DATE [ = '2000/1/1' ] },
-- -- DECLARE myDate = DATE('2000/1/1'),
-- SELECT * FROM students WHERE birth_date >DATE('2000/1/1');
