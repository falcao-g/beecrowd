for i in range(int(input())):
    pop1, pop2, grow1, grow2 = map(float, input().split())

    cont = 0
    while (cont <= 100):
        pop1 += int((pop1 * grow1) / 100)
        pop2 += int((pop2 * grow2) / 100)
        cont += 1
        if (pop1 > pop2):
            break
    
    if (cont > 100):
        print("Mais de 1 seculo.")
    else:
        print(f"{cont} anos.")