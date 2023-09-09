SELECT
		departamento.nome AS "Nome Departamento",
		COUNT(salarios.lotacao) AS "Numero de Empregados",
		ROUND(AVG(salarios.salario), 2) AS "Media Salarial",
		ROUND(MAX(salarios.salario), 2) AS "Maior Salario",
		CASE WHEN MIN(salarios.salario) = 0.00 THEN 0
			 ELSE ROUND(MIN(salarios.salario), 2)
		END AS "Menor Salario"
	FROM (
		SELECT
		venc_agrupados.lotacao,
		ROUND(SUM(total_vencimentos) - COALESCE(SUM(total_descontos), 0), 2) AS salario
		FROM (

			SELECT
				empregado.matr,
				empregado.lotacao,
				COALESCE(SUM(vencimento.valor), 0) AS total_vencimentos
			FROM empregado
			LEFT JOIN emp_venc
				ON empregado.matr = emp_venc.matr
			LEFT JOIN vencimento
				ON emp_venc.cod_venc = vencimento.cod_venc
			GROUP BY empregado.matr, empregado.lotacao

			) AS venc_agrupados

			LEFT JOIN (

				SELECT
					empregado.matr,
					empregado.lotacao,
					COALESCE(SUM(desconto.valor), 0) AS total_descontos
				FROM empregado
				LEFT JOIN emp_desc
					ON empregado.matr = emp_desc.matr
				LEFT JOIN desconto
					ON emp_desc.cod_desc = desconto.cod_desc
				GROUP BY empregado.matr, empregado.lotacao

			) AS desc_agrupados
				ON venc_agrupados.matr = desc_agrupados.matr
			GROUP BY venc_agrupados.matr, venc_agrupados.lotacao
		) AS salarios
	INNER JOIN departamento
		ON salarios.lotacao = departamento.cod_dep
	GROUP BY departamento.nome
	ORDER BY "Media Salarial" DESC