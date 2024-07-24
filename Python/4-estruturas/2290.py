import sys

while True:
    try:
        n = int(sys.stdin.readline())
    except:
        break

    if n == 0:
        break

    numeros = [int(x) for x in sys.stdin.readline().split()]
    resp = []
    numeros.sort()

    i = 0
    while i < n:
        if i == n-1:
            resp.append(numeros[i])
            break

        if numeros[i] ^ numeros[i+1] == 0:
            i += 1
        else:
            resp.append(numeros[i])
            if i == n - 2:
                resp.append(numeros[i+1])
        i += 1

    resp.sort()
    sys.stdout.write(f"{resp[0]} {resp[1]}\n")
