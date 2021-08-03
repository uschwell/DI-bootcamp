-- Database: public

-- DROP DATABASE public;

-- CREATE DATABASE public
--     WITH 
--     OWNER = postgres
--     ENCODING = 'UTF8'
--     LC_COLLATE = 'English_Israel.1252'
--     LC_CTYPE = 'English_Israel.1252'
--     TABLESPACE = pg_default
--     CONNECTION LIMIT = -1;

-- -- -- -- -- -- 1.1
-- SELECT * FROM items ORDER BY price ASC;

-- -- -- -- -- -- 1.2
-- SELECT * FROM items WHERE price>=80 ORDER BY price DESC;

-- -- -- -- -- -- 1.3
-- SELECT * FROM customers ORDER BY first_name, last_name ASC LIMIT 3;

-- -- -- -- -- -- 1.4
-- SELECT last_name FROM customers ORDER BY last_name DESC;









-- -- -- -- Note: I added two serial numbers to be primary keys on the two tables-this code should be run ONCE only
-- ALTER TABLE customers DELETE PRIMARY KEY;
-- ALTER TABLE customers ADD cust_id_s SERIAL;
-- ALTER TABLE customers ADD PRIMARY KEY (cust_id_s);

-- ALTER TABLE items DROP CONSTRAINT;
-- ALTER TABLE items ADD item_id_s SERIAL;
-- ALTER TABLE items ADD PRIMARY KEY (item_id_s);


-- -- -- -- -- -- part 2
-- CREATE TABLE purchases (
-- 	purchase_id SERIAL,
-- 	customer_id int NOT NULL,
-- 	item_id int NOT NULL,
-- 	PRIMARY KEY (purchase_id),
-- 	FOREIGN KEY (customer_id) REFERENCES customers (cust_id_s), 
-- 	FOREIGN KEY (item_id) REFERENCES items (item_id_s)
-- );

SELECT * FROM purchases;