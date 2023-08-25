input()
notas = [int(x) for x in input().split()]

conjunto_notas = set(notas)

termo = 0
frequencia = 0
for nota in conjunto_notas:
    if notas.count(nota) > frequencia:
        frequencia = notas.count(nota)
        termo = nota
    elif notas.count(nota) == frequencia:
        if nota > termo:
            termo = nota

print(termo)