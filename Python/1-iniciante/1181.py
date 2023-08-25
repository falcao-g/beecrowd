linha = int(input())
operation = input()

matriz = []
for i in range(12):
    if i > linha:
        break
    matriz.append([])
    for j in range(12):
        matriz[i].append(float(input()))

if operation == 'S':
    print(sum(matriz[linha]))
else:
    print(sum(matriz[linha]) / 12)