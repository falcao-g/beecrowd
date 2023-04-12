inicio = int(input())
fim = int(input())

if inicio > fim:
    incremento = -1
else:
    incremento = 1

soma = 0
for i in range(inicio + incremento, fim, incremento):
    if i % 2 != 0:
        soma += i
        
print(soma)