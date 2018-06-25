-- Import in hbtn_0c_0 database this table dump
-- https://s3.amazonaws.com/intranet-projects-files/holbertonschool-higher-level_programming+/272/temperatures.sql
-- Displays the average temperature by city ordered by temperature (descending)
SELECT city, AVG(value) AS avg_temp FROM temperatures GROUP BY city ASC;
