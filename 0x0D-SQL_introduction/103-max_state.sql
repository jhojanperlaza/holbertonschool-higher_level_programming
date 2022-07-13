-- script that displays the average temperature (Fahrenheit)
-- by city ordered by temperature (descending)
SELECT state, MAX(value) 'max_temp' FROM temperatures GROUP BY state ORDER BY max_temp DESC;
