maior = 0
indice = 0
for i in range(100):
    numero = int(input())

    if numero > maior:
        maior = numero
        indice = i + 1
        
print(maior)
print(indice)