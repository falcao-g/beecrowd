n = int(input())
pecas = set(map(int, input().split()))

for i in range(1, n + 1):
    if i not in pecas:
        print(i)
        break