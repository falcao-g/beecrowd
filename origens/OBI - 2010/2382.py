import math

L, A, P, R = map(int, input().split())

diagonal = math.sqrt(L**2 + A**2 + P**2)
diameter = 2 * R

if diameter >= diagonal:
    print('S')
else:
    print('N')