SELECT
	title,
	TRUNC(cost, 3) AS modified_price
FROM
	books

-- solution 2
-- SELECT
--     title,
--     TO_CHAR(cost, 'FM999999999.000') AS modified_price
-- FROM
--     books
-- ORDER BY
--     id;