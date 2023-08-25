import sys

while True:
    if '0' in sys.stdin.readline().split():
        break

    d_atacantes = [int(x) for x in sys.stdin.readline().split()]
    d_defensores = [int(x) for x in sys.stdin.readline().split()]

    sys.stdout.write('Y\n' if min(d_atacantes) < sorted(d_defensores)[1] else 'N\n')