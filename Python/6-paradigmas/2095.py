from collections import deque
import sys

n = int(sys.stdin.readline())

sol1 = [int(x) for x in sys.stdin.readline().split()]
sol2 = [int(x) for x in sys.stdin.readline().split()]

fila1 = deque(sorted(sol1, reverse=True))
fila2 = deque(sorted(sol2, reverse=True))

vitorias = 0
while fila1 and fila2:
    inimigo = fila1.popleft()
    atual = fila2.popleft()
    while atual <= inimigo and fila1:
        inimigo = fila1.popleft()
    if atual > inimigo:
        vitorias += 1

sys.stdout.write(f"{vitorias}\n")
