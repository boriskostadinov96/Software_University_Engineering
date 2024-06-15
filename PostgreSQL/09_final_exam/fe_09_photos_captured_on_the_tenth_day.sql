SELECT
    LEFT(description || '...', 10) AS summary,
    TO_CHAR(capture_date, 'DD.MM HH24:MI')
FROM
    photos
WHERE
    EXTRACT(DAY FROM capture_date) = 10
ORDER BY
    capture_date DESC;