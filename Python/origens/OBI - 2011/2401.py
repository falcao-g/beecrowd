atual = 1
for _ in range(int(input())):
    n, op = input().split()
    n = int(n)
    if op == '*':
        atual *= n
    else:
        atual /= n
print('{:.0f}'.format(atual))