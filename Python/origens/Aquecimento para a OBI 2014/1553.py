from collections import Counter

while True:
    n, k = map(int, input().split())
    
    if n == 0 and k == 0:
        break

    perguntas = [int(x) for x in input().split()]
    contador = Counter(perguntas)
    
    frequentes = 0
    for cont in contador.values():
        if cont >= k:
            frequentes += 1

    print(frequentes)
