SELECT
	title
	FROM 
		books
WHERE
	title LIKE 'The%'

-- solution 2
-- SELECT
-- 	title
-- 	FROM 
-- 		books
-- WHERE
-- 	SUBSTRING(title, 1, 3) = 'The'

-- solution 3
-- SELECT
-- 	title
-- 	FROM 
-- 		books
-- WHERE
-- 	LEFT(title, 3) = 'The'