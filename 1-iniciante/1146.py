numero = int(input())

while numero != 0:
    numeros = []
    for i in range(1, numero+1):
        numeros.append(str(i))
    print(' '.join(numeros))
    numero = int(input())