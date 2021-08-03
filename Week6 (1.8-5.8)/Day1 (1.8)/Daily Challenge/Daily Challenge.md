-- CREATE DATABASE "HollyWood"
--     WITH 
--     OWNER = postgres
--     ENCODING = 'UTF8'
--     LC_COLLATE = 'English_Israel.1252'
--     LC_CTYPE = 'English_Israel.1252'
--     TABLESPACE = pg_default
--     CONNECTION LIMIT = -1;

-- COMMENT ON DATABASE "HollyWood"
--     IS 'my 2nd attempt';

-- CREATE TABLE actors(
--  actor_id SERIAL PRIMARY KEY,
--  first_name VARCHAR (50) NOT NULL,
--  last_name VARCHAR (100) NOT NULL,
--  age DATE NOT NULL,
--  number_oscars SMALLINT NOT NULL
-- );

-- INSERT INTO actors (first_name, last_name, age, number_oscars)
-- VALUES('Matt','Damon','08/10/1970', 5);

-- INSERT INTO actors (first_name, last_name, age, number_oscars)
-- VALUES(' George',' Clooney','06/05/1961 ', 2);

-- INSERT INTO actors (first_name, last_name, age, number_oscars)
-- VALUES(' Gal',' Gadot','30/4/1985 ', 20);

-- INSERT INTO actors (first_name, last_name, age, number_oscars)
-- VALUES(' Yvonne',' Strahovski','30/7/1982 ', 0);

-- INSERT INTO actors (first_name, last_name, age, number_oscars)
-- VALUES(' Samwise',' Gamgee','1/1/1960 ', 0),
-- (' Frodo',' Baggins','1/2/1960 ', 0),
-- (' Gandalf',' The Grey','1/1/0010 ', 0);



-- -- -- -- -- Part 1
-- SELECT COUNT(*) FROM actors

-- -- -- -- -- Part 2
-- -- -- -- Answer: it will cause 'syntax errors', since the Variables were declared as "NOT NULL"
-- INSERT INTO actors (first_name, last_name, age, number_oscars)
-- VALUES('','','', );