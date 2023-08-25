import sys
pedras, sapos = map(int, sys.stdin.readline().split())
pedras = [0 for _ in range(pedras)]
for i in range(sapos):
    pos, pulo = map(int, sys.stdin.readline().split())
    pos -= 1
    posi = pos
    while pos < len(pedras):
        pedras[pos] = 1
        pos += pulo
    while posi >= 0:
        pedras[posi] = 1
        posi -= pulo

for j in range(len(pedras)):
    sys.stdout.write(f'{pedras[j]}\n')