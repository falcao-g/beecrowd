quebra, total = map(int, input().split(" "))

numeros = []
for i in range(1, total+1):
    numeros.append(str(i))
    if i % quebra == 0:
        print(' '.join(numeros))
        numeros = []