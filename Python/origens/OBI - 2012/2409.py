import sys
a, b, c = map(int, sys.stdin.readline().split())
h, l = map(int, sys.stdin.readline().split())
sys.stdout.write('S\n' if (a < h and b < l) or (a < h and c < l) or (b < h and c < l) or (a < l and b < h) or (a < l and c < h) or (b < l and c < h) else 'N\n')