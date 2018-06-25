-- Import in hbtn_0c_0 database this table dump
-- https://s3.amazonaws.com/intranet-projects-files/holbertonschool-higher-level_programming+/272/temperatures.sql
-- Displays the top 3 of cities temperature during July and August ordered by temperature (descending)
SELECT city, AVG(value) AS avg_temp FROM temperatures
WHERE month=8 OR month=7
GROUP BY city ORDER BY AVG(VALUE) DESC LIMIT 3;
