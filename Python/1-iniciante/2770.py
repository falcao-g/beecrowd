import sys

while True:
    line = sys.stdin.readline()
    if not line:
        break
    x, y, amount = map(int, line.split())

    for i in range(amount):
        a, b = map(int, sys.stdin.readline().split())
        sys.stdout.write('Sim\n' if (a<=x and b<=y) or (a<=y and b<=x) else 'Nao\n')