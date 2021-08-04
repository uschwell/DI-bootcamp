-- Database: dvdrental

-- -- DROP DATABASE dvdrental;

-- CREATE DATABASE dvdrental
--     WITH 
--     OWNER = postgres
--     ENCODING = 'UTF8'
--     LC_COLLATE = 'English_Israel.1252'
--     LC_CTYPE = 'English_Israel.1252'
--     TABLESPACE = pg_default
--     CONNECTION LIMIT = -1;




-- -- -- -- -- part 1
-- -- -- -- -- wasn't sure what you meant by "all columns"-I assumed its one of these two queries

--SELECT * FROM customer;

--SELECT * FROM customer LIMIT 0;


-- -- -- -- -- part 2
-- SELECT first_name, last_name AS full_name
-- FROM customer;



-- -- -- -- -- part 3
--SELECT create_date FROM customer;


-- -- -- -- -- part 4
-- -- -- -- if I understood correctly, you guy swanted all the relevant PERSONAl information about the customer- not the WHOLE table
-- SELECT customer_id, first_name, last_name, email, address_id, active FROM customer
-- ORDER BY first_name ASC;



-- -- -- -- -- part 5
-- SELECT film_id, title, description, release_year, rental_rate FROM film
-- ORDER BY rental_rate ASC;


-- -- -- -- -- part 6
-- SELECT address, phone FROM address WHERE district = 'Texas';


-- -- -- -- -- part 7
--SELECT * FROM film WHERE film_id= 15 OR film_id=150;



-- -- -- -- -- part 8
-- -- -- -- -- Note: I tried to accept user input for favorite movie- it only sometimes works....

-- declare
--   name VARCHAR(10);
-- begin
--   name := '&k';
--   dbms_output.put_line('Name is: ' || name);
-- end;
-- /


-- -- -- -- --For when my user input DOESNT work

-- DECLARE @myName AS VARCHAR(50)='Agent Truman'
-- SELECT film_id, title, description, length,rental_rate FROM film;
-- -- -- -- -- OR
--SELECT film_id, title, description, length,rental_rate FROM film WHERE film_id=myName;


-- -- -- -- -- Otherwise......
--SELECT film_id, title, description, length,rental_rate FROM film WHERE film_id=name;



-- -- -- -- -- part 9
-- -- -- -- -- same as 8- two versions, one that assume we already know the favorite movie,
-- -- -- -- -- and one for when we succesfully input a favorite movie

-- SELECT film_id, title, description, length,rental_rate FROM film;
-- -- -- -- -- OR
-- -- --SELECT film_id, title, description, length,rental_rate FROM film WHERE ''%__film_id%'' LIKE ''%__myName%'';

-- -- -- -- -- Otherwise.....
-- -- -- SELECT film_id, title, description, length,rental_rate FROM film WHERE '__film_id%' LIKE '%__myName%';




-- -- -- -- -- part 10
--SELECT title FROM film ORDER BY rental_rate ASC LIMIT 10;


-- -- -- -- -- part 11
-- SELECT * FROM film
-- ORDER BY rental_rate ASC
-- OFFSET (10) ROWS FETCH NEXT (10) ROWS ONLY

-- -- -- -- -- part 12
-- SELECT customer.customer_id, payment.payment_date, payment.amount
-- FROM customer
-- RIGHT JOIN payment
-- ON customer.customer_id = payment.customer_id;



-- -- -- -- -- part 13
-- -- -- -- -- my assumption- from rental-if Return Date is null, the film hasnt been returned yet
-- -- -- -- -- I retrieve the film NAME from the film table
-- -- -- -- -- I included the inventory_id so that the emplyees can locate the film


-- SELECT film.title, rental.rental_id, inventory.inventory_id
-- FROM rental, film
-- RIGHT JOIN inventory
-- ON film.film_id = inventory.film_id
-- WHERE rental.return_date IS NULL;




-- -- -- -- -- part 14
-- SELECT city.city, country.country
-- FROM city, country
-- WHERE country.country_id=city.city_id;




