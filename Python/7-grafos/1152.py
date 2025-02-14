def find(x):
    # se x é pai de si mesmo, ele é o patriarca
    if x != pai[x]:
        pai[x] = find(pai[x])
    return pai[x]


def join(x, y):
    x = find(x)
    y = find(y)

    # se x e y já estão na mesma família, não precisamos fazer nada
    if x == y:
        return

    # se x e y não estão na mesma família, vamos juntar as duas
    # fazendo com que o patriarca da maior família seja o pai do patriarca da menor família
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


while True:
    n, m = map(int, input().split())

    if n == 0 and m == 0:
        break

    # inicialmente, cada vertice é pai de si mesmo
    pai = {i: i for i in range(n + 1)}
    peso = {i: 0 for i in range(n + 1)}  # usamos os pesos para otimizar o find

    arestas = [{"x": 0, "y": 0, "dist": 0} for _ in range(m)]

    for i in range(m):
        x, y, dist = map(int, input().split())
        arestas[i] = {"x": x, "y": y, "dist": dist}

    mst = kruskal(arestas)

    peso_total = sum(aresta["dist"] for aresta in arestas)
    peso_mst = sum(aresta["dist"] for aresta in mst)

    print(peso_total - peso_mst)
