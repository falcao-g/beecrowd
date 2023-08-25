coluna = int(input())
operation = input()

matriz = []
for i in range(12):
    matriz.append([])
    for j in range(12):
        matriz[i].append(float(input()))

if operation == 'S':
    soma = 0
    for i in range(12):
        soma += matriz[i][coluna]
    print(f'{soma:.1f}')
else:
    soma = 0
    for i in range(12):
        soma += matriz[i][coluna]
    print(f"{soma / 12:.1f}")