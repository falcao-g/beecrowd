SELECT m.id, m.name 
FROM movies m 
INNER JOIN genres g ON (g.id = m.id_genres) 
WHERE g.description = 'Action'