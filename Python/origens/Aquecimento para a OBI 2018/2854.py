m, n = map(int, input().split())
entrada = [input() for _ in range(n)]

pessoas = set()
for i in entrada:
    i = i.split()
    pessoas.add(i[0])
    pessoas.add(i[-1])

parente = {i: i for i in pessoas}
peso = {i: 0 for i in pessoas}

def find(x):
    if x != parente[x]:
        parente[x] = find(parente[x])
    return parente[x]


def join(x, y):
    x = find(x)
    y = find(y)

    if x == y:
        return

    if peso[x] < peso[y]:
        parente[x] = y

    if peso[x] > peso[y]:
        parente[y] = x

    if peso[x] == peso[y]:
        parente[x] = y
        peso[y] += 1


for ent in entrada:
    nome1, rel, nome2 = ent.split()
    join(nome1, nome2)

print(len(set([find(i) for i in parente])))