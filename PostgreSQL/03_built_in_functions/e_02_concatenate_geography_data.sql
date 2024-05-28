CREATE VIEW view_continents_countries_currencies_details AS
SELECT
	CONCAT(
	con.continent_name,
	': ',
	con.continent_code) AS continent_details,
	
	CONCAT_WS(' - ',
	cou.country_name,
	cou.capital,
	cou.area_in_sq_km,
	'km2') AS country_information,

	CONCAT(
	cur.description,
	' (',
	cur.currency_code,
	')'
	) AS currencies

FROM 
	continents AS con,
	countries AS cou,
	currencies AS cur

WHERE
	con.continent_code = cou.continent_code
		AND
	cou.currency_code = cur.currency_code

ORDER BY 
	country_information,
	currencies

-- solution 2
-- CREATE VIEW view_continents_countries_currencies_details AS
-- SELECT
--     CONCAT(continents.continent_name, ': ', continents.continent_code) AS continent_details,
--     CONCAT_WS(' - ', countries.country_name, countries.capital, countries.area_in_sq_km, 'km2') AS country_information,
--     CONCAT(currencies.description, ' (', currencies.currency_code, ')') AS currencies
-- FROM
--     continents
-- JOIN
--     countries ON continents.continent_code = countries.continent_code
-- JOIN
--     currencies ON countries.currency_code = currencies.currency_code
-- ORDER BY
--     country_information ASC,
--     currencies ASC;