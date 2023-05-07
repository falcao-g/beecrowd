total = 0
atual = 0
for _ in range(int(input())):
    num = int(input())
    if num != atual:
        total += 1
        atual = num

print(total)