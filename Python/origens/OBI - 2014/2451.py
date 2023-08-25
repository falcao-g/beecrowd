import sys

tamanho = int(sys.stdin.readline())
map = []
for i in range(tamanho):
    map.append(sys.stdin.readline().rstrip())

half = tamanho ** tamanho // 2

highest = 0
now = 0
for i in range(len(map)):
    if now >= half:
        break

    if i % 2 == 0:
        start = 0
        end = len(map[i])
        step = 1
    else:
        start = len(map[i]) - 1
        end = -1
        step = -1
    for j in range(start, end, step):
        if map[i][j] == 'o':
            now += 1
        
        if map[i][j] == 'A':
            if now > highest:
                highest = now
            now = 0

if now > highest:
    highest = now
        
sys.stdout.write(f'{highest}\n')