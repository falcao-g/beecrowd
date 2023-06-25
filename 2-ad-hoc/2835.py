def Analisa(vet):
    possivel = True
    menor = min(vet)

    if menor > 8:
        possivel = False
        return possivel

    for i in range(len(vet)-1):
        if abs(vet[i+1] - vet[i]) > 8:
            possivel = False
            break
    return possivel

input()
vetor = [int(x) for x in input().split()]
print('S' if Analisa(sorted(vetor)) else 'N')