import sys

linhas, colunas = map(int, sys.stdin.readline().split())
map = []
for _ in range(linhas):
    map.append(sys.stdin.readline().strip())

total = 0
for i in range(linhas):
    for j in range(colunas):
        if map[i][j] == '#':
            if i == 0 or map[i-1][j] == '.':
                total += 1
            elif j == 0 or map[i][j-1] == '.':
                total += 1
            elif i == linhas-1 or map[i+1][j] == '.':
                total += 1
            elif j == len(map[i])-1 or map[i][j+1] == '.':
                total += 1

sys.stdout.write(str(total) + '\n')