while (n := int(input())) != 0:
    magnitudes = [int(x) for x in input().split()]
    picos = 0

    for m in range(0, n):
        antecessor = m-1
        sucessor = m+1 if (m+1 < n) else 0

        if  magnitudes[antecessor] > magnitudes[m] < magnitudes[sucessor]:
            picos += 1
            continue
        elif magnitudes[antecessor] < magnitudes[m] > magnitudes[sucessor]:
            picos += 1
            continue

    print(picos)
