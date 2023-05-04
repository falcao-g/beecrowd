n, m = map(int, input().split())
pinos = [int(x) for x in input().split()]

movimentos = 0
for i in range(n-1):
    while pinos[i] > m:
        pinos[i] -= 1
        pinos[i + 1] -= 1
        movimentos += 1

    while pinos[i] < m:
        pinos[i] += 1
        pinos[i + 1] += 1
        movimentos += 1

print(movimentos)