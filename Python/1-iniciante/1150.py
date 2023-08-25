x = int(input())
z = int(input())

while z <= x:
    z = int(input())

cont = 0
soma = 0

while soma < z:
    soma += x
    cont += 1
    x += 1

print(cont)