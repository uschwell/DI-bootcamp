-- Database: dvdrental

-- DROP DATABASE dvdrental;

-- CREATE DATABASE dvdrental
--     WITH 
--     OWNER = postgres
--     ENCODING = 'UTF8'
--     LC_COLLATE = 'English_Israel.1252'
--     LC_CTYPE = 'English_Israel.1252'
--     TABLESPACE = pg_default
--     CONNECTION LIMIT = -1;

-- -- -- -- -- Assumption: I am working off the databases we downloaded/installed yesterday

-- -- -- -- -- part 1
-- SELECT distinct language.name AS film_languages
-- FROM language,film
-- WHERE language.language_id=film.language_id;


-- -- -- -- -- part 2
-- film title, description, and language name

-- -- -- -- -- part 2.1
-- SELECT film.title, film.description,language.name
-- FROM film
-- LEFT JOIN language
-- ON film.language_id = language.language_id; 


-- -- -- -- -- part 2.2
-- SELECT film.title, film.description,language.name
-- FROM language
-- LEFT JOIN film
-- ON film.language_id = language.language_id;



-- -- -- -- -- part 3

-- CREATE TABLE new_film(
-- newFilm_id SERIAL, name VARCHAR(225),
-- 	PRIMARY KEY(newFilm_id)
-- );

-- INSERT INTO new_film(name) 
-- Values
-- ('Aaaa'),('Bbbb'),('Cccc'),('Dddd'),('Eeee'),('Ffff'),('Gggg'),('Hhhh');


-- SELECT * FROM new_film;



-- -- -- -- -- part 4

-- CREATE TABLE customer_review(
-- 	review_id SERIAL NOT NULL, film_id INTEGER, language_id INTEGER,
-- 	title VARCHAR(100), score SMALLINT, review_text TEXT, last_update DATE,
-- 	PRIMARY KEY(review_id),
-- 	FOREIGN KEY(film_id) REFERENCES new_film(newfilm_id),
-- 	FOREIGN KEY(language_id) REFERENCES language(language_id)
-- );



-- -- -- -- -- part 5
-- INSERT INTO customer_review(film_id, language_id, title, score, review_text, last_update) 
-- VALUES
-- (1,1,'Aa review', 98, 'I liked this film', '2021-8-3'),
-- (2,1, 'Bb review',90, 'This movie was not quite as good','2021-8-3')
-- ;


-- -- -- -- -- part 6
-- -- -- I may have misunderstood what you guys wanted here. Since I defined several keys in customer_review
-- -- -- with the help of new_film. I am now NOT ALLOWED to delete values from new_film. (Since it can alter the child table)
-- -- -- was this what you wanted to prove?
-- DELETE FROM new_film WHERE new_film.newfilm_id=2;
-- SELECT * FROM customer_review;











+