import sys

albumX, albumY = map(int, sys.stdin.readline().split())
x1, y1 = map(int, sys.stdin.readline().split())
x2, y2 = map(int, sys.stdin.readline().split())

sys.stdout.write(f'S\n' if (x1 + x2 <= albumX and max(y1, y2) <= albumY) or (y1 + y2 <= albumX and max(x1, x2) <= albumY) or (x1 + y2 <= albumX and max(y1, x2) <= albumY) or (y1 + x2 <= albumX and max(x1, y2) <= albumY) or (y1 + y2 <= albumY and max(x1, x2) <= albumX) or (x1 + y2 <= albumY and max(y1, x2) <= albumX) or (y1 + x2 <= albumY and max(x1, y2) <= albumX) else 'N\n')