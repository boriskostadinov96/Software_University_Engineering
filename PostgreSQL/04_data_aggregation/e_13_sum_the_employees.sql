SELECT
	COUNT(CASE department_id WHEN 1 THEN '' ELSE NULL END) "Engineering",
	COUNT(CASE department_id WHEN 2 THEN '' ELSE NULL END) "Tool Design",
	COUNT(CASE department_id WHEN 3 THEN '' ELSE NULL END) "Sales",
	COUNT(CASE department_id WHEN 4 THEN '' ELSE NULL END) "Marketing",
	COUNT(CASE department_id WHEN 5 THEN '' ELSE NULL END) "Purchasing",
	COUNT(CASE department_id WHEN 6 THEN '' ELSE NULL END) "Research and Development",
	COUNT(CASE department_id WHEN 7 THEN '' ELSE NULL END) "Production"
FROM 
	employees