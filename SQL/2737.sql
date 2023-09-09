SELECT name, customers_number
FROM (
  SELECT name, customers_number, 1 AS order_column
  FROM lawyers
  WHERE customers_number = (SELECT MAX(customers_number) FROM lawyers)

  UNION

  SELECT name, customers_number, 2 AS order_column
  FROM lawyers
  WHERE customers_number = (SELECT MIN(customers_number) FROM lawyers)

  UNION

  SELECT 'Average' AS name, ROUND(AVG(customers_number)), 3 AS order_column
  FROM lawyers
) AS subquery
ORDER BY order_column