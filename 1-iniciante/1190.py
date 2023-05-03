operation = input()

matriz = []
for i in range(12):
    matriz.append([])
    for j in range(12):
        matriz[i].append(float(input()))

soma = 0
total = 0
for i in range(1, 11):
    for j in range(12):
        if i <= 5:
            if j > 11-i:
                soma += matriz[i][j]
                total += 1
        else:
            if j > i:
                soma += matriz[i][j]
                total += 1

if operation == 'S':
    print(f'{soma:.1f}')
else:
    print(f'{soma / total:.1f}')