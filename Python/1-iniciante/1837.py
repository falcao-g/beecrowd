a, b = map(int, input().split())

q = a // b
r = a % b

if a < 0 or b < 0:
    r = 0
    for r in range(abs(b)):
        if (a - r) % b == 0:
            break
    q = (a - r) // b

print(q, r)