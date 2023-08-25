x = int(input())

while x != 0:
    inicio = x
    if x % 2 != 0:
        inicio += 1
        
    soma = 0
    for i in range(inicio, inicio + 10, 2):
        soma += i
    print(soma)
    x = int(input())