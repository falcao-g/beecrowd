grenais = 0
inter = 0
gremio = 0
empates = 0

while True:
    golsInter, golsGremio = map(int, input().split())
    grenais += 1
    if golsInter > golsGremio:
        inter += 1
    elif golsInter < golsGremio:
        gremio += 1
    else:
        empates += 1
    print('Novo grenal (1-sim 2-nao)')
    novo = int(input())
    if novo == 2:
        break

print('{} grenais'.format(grenais))
print('Inter:{}'.format(inter))
print('Gremio:{}'.format(gremio))
print('Empates:{}'.format(empates))

if inter > gremio:
    print('Inter venceu mais')
elif inter < gremio:
    print('Gremio venceu mais')
else:
    print('Nao houve vencedor')