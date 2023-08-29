import math

n, p = map(int, input().split())

t = n * p

for i in range(1, 10):
    if i == 9:
        print(math.ceil((t * i) / 10))
        break
    print(math.ceil((t * i) / 10), end=' ')