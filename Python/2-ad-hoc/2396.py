c, v = map(int, input().split())

carros = {}

for i in range(1, c+1):
    carros[i] = sum([int(volta) for volta in input().split()])

carros = sorted(carros.items(), key=lambda x: x[1])

print(carros[0][0])
print(carros[1][0])
print(carros[2][0])