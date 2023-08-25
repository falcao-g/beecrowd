def encontraMaior(n, arvore):
    distanciaAuxiliar = float('-inf')
    for i in range(n):
        distanciaAtual = arvore[0] + arvore[i] + i
        if distanciaAuxiliar < distanciaAtual:
            distanciaAuxiliar = distanciaAtual
            predioMaior = i
    return predioMaior

n = int(input())
predios = [int(a) for a in input().split()]
maiorPredio = encontraMaior(n, predios)
distanciaMaxima = float('-inf')

for i in range(n):
    if i != maiorPredio:
        distanciaAuxiliar = predios[i] + abs(maiorPredio-i) + predios[maiorPredio]
        if distanciaAuxiliar > distanciaMaxima:
            distanciaMaxima = distanciaAuxiliar

print(distanciaMaxima)