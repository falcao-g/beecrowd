import collections, sys

while True:
    n = int(sys.stdin.readline())
    if n == 0:
        break
    
    # inicializa o grafo como um dicionário vazio
    graph = {i: set() for i in range(1, 1001)}
    
    line = sys.stdin.readline().split()

    # adiciona as arestas ao grafo
    for i in range(len(line)):
        x, y = map(int, line[i][1:-1].split(','))
        graph[x].add(y)
        graph[y].add(x)
    
    # faz a busca em largura a partir do nó 1
    visited = set()
    queue = collections.deque([1])
    while queue:
        node = queue.popleft()
        visited.add(node)
        for neighbor in graph[node]:
            if neighbor not in visited:
                queue.append(neighbor)
    
    # imprime o número de nós visitados (incluindo o nó 1)
    sys.stdout.write(f'{len(visited)}\n')
