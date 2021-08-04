-- -- -- -- --Question1:
-- CREATE TABLE FirstTab (
--      id integer, 
--      name VARCHAR(10)
-- );

-- INSERT INTO FirstTab VALUES
-- (5,'Pawan'),
-- (6,'Sharlee'),
-- (7,'Krish'),
-- (NULL,'Avtaar');

-- SELECT * FROM FirstTab;

-- CREATE TABLE SecondTab (
--     id integer 
-- );

-- INSERT INTO SecondTab VALUES
-- (5),
-- (NULL);


-- SELECT * FROM SecondTab;



-- -- -- Note:where needed I add the ; to make the commands legal. I assume we dont want "unable to execute...."
-- -- -- for every command.
-- -- -- -- --Question1:
-- -- -- -- Assumption:
-- count
-- 0

-- -- -- -- Check:
-- SELECT COUNT(*) 
-- FROM FirstTab AS ft WHERE ft.id NOT IN ( SELECT id FROM SecondTab WHERE id IS NULL );


-- -- -- -- --Question2:
-- -- -- -- Assumption:
-- count
-- 2

-- -- -- -- Check:
--     SELECT COUNT(*) 
--     FROM FirstTab AS ft WHERE ft.id NOT IN ( SELECT id FROM SecondTab WHERE id = 5 )



-- -- -- -- --Question3:
-- -- -- -- Assumption:
-- count
-- 0

-- -- -- -- Check:
--     SELECT COUNT(*) 
--     FROM FirstTab AS ft WHERE ft.id NOT IN ( SELECT id FROM SecondTab )




-- -- -- -- --Question4:
-- -- -- -- Assumption:
-- count
-- 2

-- -- -- -- Check:
--     SELECT COUNT(*) 
--     FROM FirstTab AS ft WHERE ft.id NOT IN ( SELECT id FROM SecondTab WHERE id IS NOT NULL )








-- SELECT * FROM firsttab;
-- SELECT * FROM secondtab;


