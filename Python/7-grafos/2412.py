import collections, sys, math

n, d = map(int, sys.stdin.readline().split())

# lê as coordenadas das árvores
trees = []
for i in range(n):
    x, y = map(int, sys.stdin.readline().split())
    trees.append((x, y))

# cria o grafo
graph = {i: [] for i in range(n)}

# adiciona as arestas ao grafo
for i in range(n):
    for j in range(i+1, n):
        dist = math.sqrt((trees[j][0] - trees[i][0])**2 + (trees[j][1] - trees[i][1])**2)
        if dist <= d:
            graph[i].append(j)
            graph[j].append(i)

# faz a busca em largura
visited = [False] * n
queue = collections.deque()
queue.append(0)
visited[0] = True
while queue:
    node = queue.popleft()
    for neighbor in graph[node]:
        if not visited[neighbor]:
            visited[neighbor] = True
            queue.append(neighbor)

sys.stdout.write('S\n' if all(visited) else 'N\n')