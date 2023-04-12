for i in range(int(input())):
    x, y = map(int, input().split())
    soma = 0
    cont = 0
    while cont < y:
        if x % 2 != 0:
            soma += x
            cont += 1
        x += 1
    print(soma)