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


def kruskal(arestas):
    arestas.sort(key=lambda a: a["dist"])

    mst = []
    for aresta in arestas:
        u = aresta["x"]
        v = aresta["y"]
        if find(u) != find(v):
            mst.append(aresta)
            join(u, v)

    return mst


def kruskal_invertido(arestas):
    arestas.sort(key=lambda a: a["dist"], reverse=True)

    mst = []
    for aresta in arestas:
        u = aresta["x"]
        v = aresta["y"]
        if find(u) != find(v):
            mst.append(aresta)
            join(u, v)

    return mst


n = int(input())

pai = {i: i for i in range(1, n + 1)}
peso = {i: 0 for i in range(1, n + 1)}

arestas = []

while True:
    try:
        x, y, dist = map(int, input().split())
        arestas.append({"x": x, "y": y, "dist": dist})
    except EOFError:
        break


mst = kruskal(arestas)
pai = {i: i for i in range(1, n + 1)}
peso = {i: 0 for i in range(1, n + 1)}
mst_invertido = kruskal_invertido(arestas)

peso_max = sum(aresta["dist"] for aresta in mst_invertido)
peso_min = sum(aresta["dist"] for aresta in mst)

print(peso_max)
print(peso_min)
