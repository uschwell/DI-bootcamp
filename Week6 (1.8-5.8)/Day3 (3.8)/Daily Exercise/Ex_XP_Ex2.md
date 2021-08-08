-- -- -- -- -- -- -- -- -- part 1
-- UPDATE film
-- SET language_id=2
-- WHERE film_id BETWEEN 5 AND 10;


-- -- -- -- helps to view the results
-- -- SELECT * FROM film
-- -- ORDER BY film_id ASC;




-- -- -- -- -- -- -- -- -- part 2
-- only 2 constraints. the customer_id, which is a PIMARY KEY, and the address_id which is a FOREIGN KEY.
-- since address_id references an address which is located in "address" (table) when we wish to insert a
-- new customer we need to use a reference (or a value-[less ideal]) that is already located in address. I.e we
-- cannot just randomly add or change the values in that specific column. (it also affect "address", but that's less relevant here)


-- -- -- -- -- -- -- -- -- part 3
-- DELETE FROM customer_review;
-- -- an easy step. since customer_review is the CHILD table. If we wanted to delete the PARENT table that would
-- -- be more difficult.


-- -- -- -- -- -- -- -- -- part 4
-- -- -- My Assumption: if the return_date is NULL then the video has not yet been returned
-- SELECT COUNT(*)
-- FROM rental
-- WHERE return_date IS NULL;



-- -- -- -- -- -- -- -- -- part 5
-- SELECT rental.rental_id, rental.rental_date, rental.inventory_id, rental.customer_id, rental.return_date, rental.staff_id,
-- rental.last_update
-- FROM rental
-- LEFT JOIN payment
-- ON rental.rental_id=payment.rental_id
-- WHERE return_date IS NULL
-- ORDER BY payment.amount DESC
-- LIMIT (10);





-- -- -- -- -- -- -- -- -- part 6.1
SELECT actor.first_name, actor.last_name, film_actor.film_id
FROM actor
LEFT JOIN film_actor
ON actor.actor_id=film_actor.actor_id
FULL OUTER JOIN film
ON film.film_id=film_id
;