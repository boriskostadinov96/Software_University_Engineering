SELECT
	first_name,
	last_name,
	EXTRACT(year FROM born) AS year
FROM 
	authors

-- solution 2
-- SELECT
-- 	first_name,
-- 	last_name,
-- 	date_part('year', born) AS year
-- FROM 
-- 	authors