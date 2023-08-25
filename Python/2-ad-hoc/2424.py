import sys
x, y = map(int, sys.stdin.readline().split())
sys.stdout.write('fora\n' if x < 0 or x > 432 or y < 0 or y > 468 else 'dentro\n')