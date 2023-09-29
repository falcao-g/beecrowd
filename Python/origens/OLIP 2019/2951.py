runas_totais, amizade_necessaria = map(int, input().split())

runas = {}

for _ in range(runas_totais):
    nome, valor = input().split()
    runas[nome] = int(valor)

amizade = 0
input()

faladas = [x for x in input().split()]

for runa in faladas:
    amizade += runas[runa]

print(amizade)
print("You shall pass!" if amizade >= amizade_necessaria else "My precioooous")