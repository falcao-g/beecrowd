t = 1
while (n := int(input())) != 0:
    total = 0
    print(f'Teste {t}')
    for i in range(n):
        dep, saq = map(int, input().split())
        total += dep
        total -= saq
        print(total)
    print('')
    t += 1