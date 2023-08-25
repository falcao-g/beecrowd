int(input())
values = [int(x) for x in input().split()]
menor = 0
posicao = 0
for index, value in enumerate(values):
    if index == 0:
        menor = value
    else:
        if menor > value:
            menor = value
            posicao = index

print(f"Menor valor: {menor}")
print(f"Posicao: {posicao}")