n = int(input())
numeros = [int(x) for x in input().split()]


if n > 2:
    escadinhas = n - 1
    ultima_diff = numeros[0] - numeros[1]

    for i in range(2, len(numeros)):
        if numeros[i-1] - numeros[i] == ultima_diff:
            escadinhas -= 1
        else:
            ultima_diff = numeros[i-1] - numeros[i]
        
    print(escadinhas)
else:
    print(1)