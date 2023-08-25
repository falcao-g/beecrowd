import math
N, L, D = map(int, input().split())
resp = L * math.ceil((N * D)/ (1000 * L))
print(f'{resp:.0f}')