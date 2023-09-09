SELECT name, case
    WHEN type = 'A' THEN 20.0
    WHEN type = 'B' THEN 70.0
    WHEN type = 'C' THEN 530.5
end AS price
FROM products
ORDER BY type ASC, id DESC