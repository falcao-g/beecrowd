for _ in range(int(input())):
    m, n = map(int, input().split())
    dicionario = {}

    for _ in range(m):
        jap = input()
        brz = input()

        dicionario[jap] = brz

    for _ in range(n):
        verso = [dicionario[x] if x in dicionario else x for x in input().split()]
        print(" ".join(verso))
    print("")
