for i in range(int(input())):
    inicio, fim = map(int, input().split(" "))
    
    inc = 1
    if inicio > fim:
        inc = -1
    
    soma = 0    
    for j in range(inicio + inc, fim, inc):
        if j % 2 != 0:
            soma += j
    print(soma)