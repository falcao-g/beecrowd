SELECT e.cpf, e.enome, d.dnome
FROM departamentos AS d 
INNER JOIN empregados AS e ON d.dnumero = e.dnumero 
LEFT JOIN trabalha AS t ON t.cpf_emp = e.cpf
LEFT JOIN projetos AS p ON t.pnumero = p.pnumero
WHERE p.pnumero IS NULL
ORDER BY e.cpf