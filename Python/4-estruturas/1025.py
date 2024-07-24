import sys

def busca_binaria(vetor, elemento):
    inicio = 0
    fim = len(vetor) - 1

    while inicio <= fim:
        meio = (inicio + fim) // 2

        if vetor[meio] == elemento:
            while vetor[meio] == elemento:
                meio -= 1
            return meio + 1
        elif vetor[meio] > elemento:
            fim = meio - 1
        else:
            inicio = meio + 1

    return -1

caso = 1
while True:
    n, q = map(int, sys.stdin.readline().split())

    if n == 0 and q == 0:
        break

    sys.stdout.write(f"CASE# {caso}:\n")

    numeros = []
    for _ in range(n):
        num = int(sys.stdin.readline())
        numeros.append(num)
    numeros.sort()

    for _ in range(q):
        alvo = int(sys.stdin.readline())
        resp = busca_binaria(numeros, alvo)
        if resp == -1:
            sys.stdout.write(f"{alvo} not found\n")
            continue
        sys.stdout.write(f"{alvo} found at {resp+1}\n")

    caso += 1
