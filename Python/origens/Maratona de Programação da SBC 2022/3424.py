n = int(input())
texto = input()
total = 0
for i in range(n):
    if i == 0:
        if texto[i] == 'a' and texto[i+1] == 'a':
            total += 1
    elif i == n-1:
        if texto[i] == 'a' and texto[i-1] == 'a':
            total += 1
    else:
        if texto[i] == 'a' and (texto[i-1] == 'a' or texto[i+1] == 'a'):
            total += 1
print(total)