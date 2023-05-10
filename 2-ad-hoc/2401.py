import sys
atual = 1
for _ in range(int(sys.stdin.readline())):
    n, op = sys.stdin.readline().split()
    n = int(n)
    if op == '*':
        atual *= n
    else:
        atual /= n
sys.stdout.write(f'{atual:.0f}\n')