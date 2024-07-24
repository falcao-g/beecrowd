import sys

while True:
    n = int(sys.stdin.readline())

    if n == 0:
        break

    numeros = [int(x) for x in sys.stdin.readline().split()]
    resp = 0
    numeros.sort()

    i = 0
    while i < n:
        if i == n-1:
            resp = numeros[i]
            break

        if numeros[i] ^ numeros[i+1] == 0:
            i += 1
        else:
            resp = numeros[i]
        i += 1

    sys.stdout.write(f"{resp}\n")
