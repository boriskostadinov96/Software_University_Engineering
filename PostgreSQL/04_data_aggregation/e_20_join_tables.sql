SELECT *
FROM
	departments as d
JOIN
	employees as e
ON
	d.id = e.department_id

-- solution 2
-- SELECT 
--     departments.*,
--     employees.*
-- FROM 
--     departments
-- INNER JOIN 
--     employees 
-- ON 
--     departments.id = employees.department_id;