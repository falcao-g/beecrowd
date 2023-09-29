import sys

n, m, p = map(int, sys.stdin.readline().split())

pai = {i: i for i in range(1, n + 1)} 
peso = {i: 0 for i in range(1, n + 1)}

def find(x):
    if x != pai[x]:
        pai[x] = find(pai[x])
    return pai[x]


def join(x, y):
    x = find(x)
    y = find(y)

    if x == y:
        return

    if peso[x] < peso[y]:
        pai[x] = y

    if peso[x] > peso[y]:
        pai[y] = x

    if peso[x] == peso[y]:
        pai[x] = y
        peso[y] += 1

for _ in range(m):
    a, b = map(int, sys.stdin.readline().split())
    join(a, b)

for _ in range(p):
    a, b = map(int, sys.stdin.readline().split())
    if find(a) == find(b):
        sys.stdout.write('Lets que lets\n')
    else:
        sys.stdout.write('Deu ruim\n')