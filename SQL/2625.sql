SELECT CONCAT(
    SUBSTRING(natural_person.cpf, 1, 3), '.', 
    SUBSTRING(natural_person.cpf, 4, 3), '.', 
    SUBSTRING(natural_person.cpf, 7, 3), '-', 
    SUBSTRING(natural_person.cpf, 10, 2)
)
FROM natural_person
INNER JOIN customers ON (natural_person.id_customers = customers.id)
