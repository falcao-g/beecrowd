for i in range(int(input())):
    nome = input()
    notas = [float(x) for x in input().split()]
    tam = len(notas)
    if tam == 1:
        print(f'{nome}: {notas[0] / 2:.1f}')
    elif tam == 2:
        print(f'{nome}: {sum(notas) / 2:.1f}')
    elif tam == 3:
        print(f'{nome}: {sum(notas)/ 3:.1f}')
    else:
        notas.sort()
        print(f'{nome}: {(notas[1] + notas[2] + notas[3]) / 3:.1f}')