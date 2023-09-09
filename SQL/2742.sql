SELECT name,
       ROUND(omega * 1.618, 3) AS "Fator N"
FROM life_registry
WHERE dimensions_id IN (SELECT id FROM dimensions WHERE name IN ('C774', 'C875'))
AND name LIKE 'Richard%'
ORDER BY omega