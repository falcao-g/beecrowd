n, k = map(int, input().split())

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


for _ in range(k):
    op, banco1, banco2 = map(str, input().split())

    if op == 'F':
        join(int(banco1), int(banco2))
    else:
        if find(int(banco1)) == find(int(banco2)):
            print('S')
        else:
            print('N')