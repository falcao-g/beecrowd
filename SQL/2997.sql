SELECT 
departamento.nome AS "Departamento",
empregado.nome AS "Empregado",
CASE
	WHEN COALESCE(SUM(vencimento.valor),0) > 0 THEN ROUND(COALESCE(SUM(vencimento.valor),0),2)
    ELSE 0
END AS "Salario Bruto",
CASE
	WHEN COALESCE(desconto.val_desc,0) > 0 THEN ROUND(COALESCE(desconto.val_desc,0),2)
    ELSE 0
END AS "Total Desconto",
CASE
	WHEN COALESCE(SUM(vencimento.valor),0) - COALESCE(desconto.val_desc,0) > 0 THEN ROUND(COALESCE(SUM(vencimento.valor),0) - COALESCE(desconto.val_desc,0),2)
    ELSE 0
END AS "Salario Liquidoaws"
FROM emp_venc 
	RIGHT JOIN empregado 
		on empregado.matr = emp_venc.matr 
	LEFT JOIN vencimento 
		on vencimento.cod_venc = emp_venc.cod_venc 
	LEFT JOIN departamento 
		on departamento.cod_dep = empregado.lotacao 
	LEFT JOIN (select empregado.matr, SUM(desconto.valor) AS val_desc
		from empregado 
			inner JOIN emp_desc 
				on emp_desc.matr = empregado.matr 
			LEFT JOIN desconto 
				on desconto.cod_desc = emp_desc.cod_desc
			GROUP BY empregado.matr) AS desconto 
				on desconto.matr = empregado.matr
GROUP BY departamento.nome, empregado.nome, desconto.val_desc, empregado.lotacao_div
ORDER BY (COALESCE(SUM(vencimento.valor),0) - COALESCE(desconto.val_desc,0)) DESC, lotacao_div DESC