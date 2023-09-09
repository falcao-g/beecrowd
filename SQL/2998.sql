SELECT clients.name, clients.investment, 
CEILING((clients.investment / AVG(DISTINCT operations.profit))) AS month_of_payback, 
(SUM(operations.profit) - clients.investment) AS return
FROM clients
INNER JOIN operations
ON clients.id = operations.client_id
WHERE operations.month in (1,2,3)
GROUP BY clients.id
HAVING (SUM(operations.profit) - clients.investment) >= 0
ORDER BY return desc;