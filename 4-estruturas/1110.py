from collections import deque

fila = deque()

while (n := int(input())):
    for i in range(n):
        fila.append(i + 1)

    print('Discarded cards:', end='')

    while len(fila) > 1:
        print(' ' + str(fila.popleft()), end='')
        fila.append(fila.popleft())
        if len(fila) > 1:
            print(',', end='')

    print('\nRemaining card: ' + str(fila[0]))

    fila.clear()